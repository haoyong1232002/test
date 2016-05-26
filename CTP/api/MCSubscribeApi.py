import sys
from time import sleep
import zmq
import snapshot_pb2 as pb
import threading
import datetime as dt

mc_host = '139.196.43.137'
mc_port = 5555
min_host = '139.196.43.137'
min_port = 5556
    
def call_back(data):
    print 'Callback....'
    print data

def action_stop_server(api):
    return 'stop'

def action_subscribe_tick(api):
    #print 'tick...'
    tick_bar = pb.future()
    while api.up:
        msg = api.sock.recv()
        tick_bar.ParseFromString(msg[msg.find('@') + 1:])
        api.callback(tick_bar)

def action_subscribe_minute(api):
    print "minute..."
    min_bar = pb.future_min_bar()
    while api.up:
        msg = api.sock.recv()
        min_bar.ParseFromString(msg[msg.find('@') + 1:])
        if min_bar.datetime.find('.') == -1:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S")
        else:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S.%f")
        min1_bars = {'instrument_id' : min_bar.instrument_id, \
                     'exchange_id' : min_bar.exchange_id, \
                     'datetime' : in_time, \
                     'open' : min_bar.open, \
                     'close' : min_bar.close, \
                     'high' : min_bar.high, \
                     'low' : min_bar.low, \
                     'volume' : min_bar.volume, \
                     'amount' : min_bar.amount}
        api.callback(min1_bars)

def action_subscribe_3minute(api):
    print "3minute..."
    min3_bars = {}
    min_bar = pb.future_min_bar()
    min3_bar = pb.future_min_bar()
    while api.up:
        msg = api.sock.recv()
        min_bar.ParseFromString(msg[msg.find('@') + 1:])
        if min_bar.datetime.find('.') == -1:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S")
        else:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S.%f")
        if min3_bars.get(min_bar.instrument_id) is None:
            min3_bars[min_bar.instrument_id] = {'instrument_id' : min_bar.instrument_id, \
                                                'exchange_id' : min_bar.exchange_id, \
                                                'datetime' : in_time, \
                                                'open' : min_bar.open, \
                                                'close' : min_bar.close, \
                                                'high' : min_bar.high, \
                                                'low' : min_bar.low, \
                                                'volume' : min_bar.volume, \
                                                'amount' : min_bar.amount}
        else:
            if min_bar.high > min3_bars[min_bar.instrument_id]['high']:
                min3_bars[min_bar.instrument_id]['high'] = min_bar.high
            if min_bar.low > min3_bars[min_bar.instrument_id]['low']:
                min3_bars[min_bar.instrument_id]['low'] = min_bar.low
            min3_bars[min_bar.instrument_id]['volume'] += min_bar.volume
            min3_bars[min_bar.instrument_id]['amount'] += min_bar.amount
            
            if not in_time.minute%3:
                api.callback(min3_bars[min_bar.instrument_id])
                min3_bars.pop(min_bar.instrument_id)
                
def action_subscribe_5minute(api):
    print "5minute..."
    min5_bars = {}
    min_bar = pb.future_min_bar()
    min5_bar = pb.future_min_bar()
    while api.up:
        msg = api.sock.recv()
        min_bar.ParseFromString(msg[msg.find('@') + 1:])
        print min_bar
        if min_bar.datetime.find('.') == -1:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S")
        else:
            in_time = dt.datetime.strptime(min_bar.datetime, "%Y-%m-%d %H:%M:%S.%f")
        if min5_bars.get(min_bar.instrument_id) is None:
            min5_bars[min_bar.instrument_id] = {'instrument_id' : min_bar.instrument_id, \
                                                'exchange_id' : min_bar.exchange_id, \
                                                'datetime' : in_time, \
                                                'open' : min_bar.open, \
                                                'close' : min_bar.close, \
                                                'high' : min_bar.high, \
                                                'low' : min_bar.low, \
                                                'volume' : min_bar.volume, \
                                                'amount' : min_bar.amount}
        else:
            print min5_bars[str(min_bar.instrument_id)]['high']
 
            if min_bar.high > min5_bars[min_bar.instrument_id]['high']:
                min5_bars[min_bar.instrument_id]['high'] = min_bar.high
            if min_bar.low > min5_bars[min_bar.instrument_id]['low']:
                min5_bars[min_bar.instrument_id]['low'] = min_bar.low
            min5_bars[min_bar.instrument_id]['volume'] += min_bar.volume
            min5_bars[min_bar.instrument_id]['amount'] += min_bar.amount

            if not in_time.minute%5:
                api.callback(min5_bars[min_bar.instrument_id])
                #min5_bars[min_bar.instrument_id].clear()
                min5_bars.pop(min_bar.instrument_id)
    
def action_default(api):
    print "No action named %s"%api
    return api

ACTIONS = {
          'STOP' : action_stop_server,
             '0' : action_subscribe_tick,
            '60' : action_subscribe_minute,
           '180' : action_subscribe_3minute,
           '300' : action_subscribe_5minute,
          }

class MCSubscribeApi (threading.Thread):
    def __init__(self, callback, host, port) :
        super(MCSubscribeApi, self).__init__()
        self.callback = callback
        self.host = host
        self.port = port
        self.up = False
        self.sub_freq = 0
        self.sub_data = None
        self.sock = zmq.Context(4).socket(zmq.SUB)

    def run(self):
        ACTIONS.get(str(self.sub_freq), action_default)(self)

    def subscribe(self, sub_data):
        self.up = sub_data[0]
        self.sub_data = sub_data[1]
        self.sub_freq = sub_data[2]
        for data in self.sub_data:
            #print data
            #self.sock.setsockopt(zmq.SUBSCRIBE, data['instrument'])
            self.sock.setsockopt(zmq.SUBSCRIBE, data)
        self.sock.connect('tcp://%s:%s' % (self.host, self.port))

    def unsubscribe(self):
        print 'unSubscribe'
        self.up = False
    
if __name__ == "__main__":
    sub_data = [1, [''], 0]
    api = MCSubscribeApi(call_back, mc_host, min_port)
    api.subscribe(sub_data)
    api.start()
    sleep(3000)
    #api.unsubscribe()
    
