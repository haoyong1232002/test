# encoding: UTF-8

import Queue
import datetime
import threading
import time
from collections import deque
import pytz
import api.MCSubscribeApi as MCApi
#import snapshot_pb2 as pb

import pyalgotrade.logger
from pyalgotrade import bar
from pyalgotrade import barfeed
from pyalgotrade import dataseries
from pyalgotrade import resamplebase
from pyalgotrade.utils import dt
from pyalgotrade.bar import Frequency
from pyalgotrade.xignite.barfeed import utcnow

logger = pyalgotrade.logger.getLogger("CTP")

def to_market_datetime(dateTime):
    timezone = pytz.timezone('Asia/Shanghai')
    return dt.localize(dateTime, timezone)

class TickDataSeries(object):
    def __init__(self):
        self.__priceDS = deque()
        self.__volumeDS = deque()
        self.__amountDS = deque()
        self.__dateTimes = deque()  # just for debug

    def reset(self):
        self.__priceDS.clear()
        self.__volumeDS.clear()
        self.__amountDS.clear()
        self.__dateTimes.clear()

    def getPriceDS(self):
        return self.__priceDS

    def getAmountDS(self):
        return self.__amountDS

    def getVolumeDS(self):
        return self.__volumeDS

    def getDateTimes(self):
        return self.__dateTimes

    def append(self, price, volume, amount, dateTime):
        assert(bar is not None)
        self.__priceDS.append(price)
        self.__volumeDS.append(volume)
        self.__amountDS.append(amount)
        self.__dateTimes.append(dateTime)

    def empty(self):
        return len(self.__priceDS) == 0

class MCApiThread(threading.Thread) :
    def __init__(self, identifiers, call_back) :
        super(MCApiThread, self).__init__()
        self.__sub_data = [1, identifiers, 0]
        self.__api = MCApi.MCSubscribeApi(call_back, '139.196.43.137', '5555')
        self.__api.subscribe(self.__sub_data)

    def run(self):
        self.__api.start()
    
    def unsubscribe(self):
        self.__api.unsubscribe()
        
class CTPPollingThread(threading.Thread):
    # Not using xignite polling thread is because two underscores functions can't be override, e.g. __wait()
    CTP_INQUERY_PERIOD = 3
    def __init__(self, identifiers):
        super(CTPPollingThread, self).__init__()
        self._identifiers = identifiers
        self._tickDSDict = {}

        for identifier in self._identifiers:
            self._tickDSDict[identifier] = TickDataSeries()

        self.__stopped = False

    def __wait(self):
        # first reset ticks info in one cycle, maybe we need save it if NO quotation in this period
        for identifier in self._identifiers:
            self._tickDSDict[identifier].reset()

        nextCall = self.getNextCallDateTime()
        
        api = MCApiThread(self._identifiers, self.get_CTP_tick_data)
        api.start()
        while not self.__stopped and utcnow() < nextCall:
            time.sleep(CTPPollingThread.CTP_INQUERY_PERIOD)
        #    data = pb.future()
        #    from random import randint
        #    from time import sleep
        #    data.last_price = randint(1,100)
        #    data.update_time = '11:10:00'
        #    data.amount = randint(1,100)
        #    data.volume = 1
        #   self.get_CTP_tick_data(data)
        #   sleep(1)
        api.unsubscribe()

    def get_CTP_tick_data(self, data):
        for identifier in self._identifiers:
            self._tickDSDict[identifier].append(data.last_price, data.volume, data.amount, data.update_time)
        #print self._tickDSDict
            
    def stop(self):
        self.__stopped = True

    def stopped(self):
        return self.__stopped

    def run(self):
        logger.debug("Thread started.")
        while not self.__stopped:
            self.__wait()
            if not self.__stopped:
                try:
                    self.doCall()
                except Exception, e:
                    logger.critical("Unhandled exception", exc_info=e)
        logger.debug("Thread finished.")

    # Must return a non-naive datetime.
    def getNextCallDateTime(self):
        raise NotImplementedError()

    def doCall(self):
        raise NotImplementedError()


class CTPBarFeedThread(CTPPollingThread):
    # Events
    ON_BARS = 1

    def __init__(self, queue, identifiers, frequency):
        super(CTPBarFeedThread, self).__init__(identifiers)
        self.__queue = queue
        self.__frequency = frequency
        self.__updateNextBarClose()

    def __updateNextBarClose(self):
        self.__nextBarClose = resamplebase.build_range(utcnow(), self.__frequency).getEnding()

    def getNextCallDateTime(self):
        return self.__nextBarClose

    def doCall(self):
        endDateTime = self.__nextBarClose
        self.__updateNextBarClose()
        bar_dict = {}

        for identifier in self._identifiers:
            try:
                if not self._tickDSDict[identifier].empty():
                    bar_dict[identifier] = self._build_bar(to_market_datetime(endDateTime), self._tickDSDict[identifier])
            except Exception, e:
                logger.error(e)

        if len(bar_dict):
            bars = bar.Bars(bar_dict)
            self.__queue.put((CTPBarFeedThread.ON_BARS, bars))

    def _build_bar(self, dateTime, ds):
        prices = ds.getPriceDS()
        volumes = ds.getVolumeDS()
        amounts = ds.getAmountDS()
    
        open_ = float(prices[0])
        high = float(max(prices))
        low = float(min(prices))
        close = float(prices[-1])
        volume = sum(int(v) for v in volumes)
        amount = sum(float(a) for a in amounts)
    
        return bar.BasicBar(dateTime, open_, high, low, close, volume, None, Frequency.DAY, amount)

def get_bar_list(df, frequency, date=None):
    bar_list = []

    end_time = df.ix[0].time
    if date is None:
        date = datetime.datetime.now()
    slice_start_time = to_market_datetime(datetime.datetime(date.year, date.month , date.day, 9, 30, 0))

    while slice_start_time.strftime("%H:%M:%S") < end_time:
        slice_end_time = slice_start_time + datetime.timedelta(seconds=frequency)

        ticks_slice = df.ix[(df.time < slice_end_time.strftime("%H:%M:%S")) &
                            (df.time >= slice_start_time.strftime("%H:%M:%S"))]

        if not ticks_slice.empty:
            open_ = ticks_slice.price.get_values()[-1]
            high = max(ticks_slice.price)
            low = min(ticks_slice.price)
            close = ticks_slice.price.get_values()[0]
            volume = sum(ticks_slice.volume)
            amount = sum(ticks_slice.amount)

            bar_list.append(bar.BasicBar(slice_start_time, open_, high, low,
                                         close, volume, 0, frequency, amount))
        else:
            bar_list.append(None)
        slice_start_time = slice_end_time

    return bar_list


class CTPLiveFeed(barfeed.BaseBarFeed):
    QUEUE_TIMEOUT = 0.01

    def __init__(self, identifiers, frequency, maxLen=dataseries.DEFAULT_MAX_LEN, replayDays=-1):
        barfeed.BaseBarFeed.__init__(self, frequency, maxLen)
        if not isinstance(identifiers, list):
            raise Exception("identifiers must be a list")

        self.__identifiers = identifiers
        self.__frequency = frequency
        self.__queue = Queue.Queue()

        self.__thread = CTPBarFeedThread(self.__queue, identifiers, frequency)
        for instrument in identifiers:
            self.registerInstrument(instrument)

    ######################################################################
    # observer.Subject interface
    def start(self):
        if self.__thread.is_alive():
            raise Exception("Already strated")

        # Start the thread that runs the client.
        self.__thread.start()

    def stop(self):
        self.__thread.stop()

    def join(self):
        if self.__thread.is_alive():
            self.__thread.join()

    def eof(self):
        return self.__thread.stopped()

    def peekDateTime(self):
        return None

    ######################################################################
    # barfeed.BaseBarFeed interface
    def getCurrentDateTime(self):
        return utcnow()

    def barsHaveAdjClose(self):
        return False

    def getNextBars(self):
        ret = None
        try:
            eventType, eventData = self.__queue.get(True, CTPLiveFeed.QUEUE_TIMEOUT)
            if eventType == CTPBarFeedThread.ON_BARS:
                ret = eventData
            else:
                logger.error("Invalid event received: %s - %s" % (eventType, eventData))
        except Queue.Empty:
            pass
        return ret

if __name__ == '__main__':
    liveFeed = CTPLiveFeed(['al1606'], 30, dataseries.DEFAULT_MAX_LEN, 2)
    liveFeed.start()

    while not liveFeed.eof():
        bars = liveFeed.getNextBars()
        if bars is not None:
            print bars['al1606'].getHigh(), bars['al1606'].getDateTime()

