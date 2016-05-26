# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snapshot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='snapshot.proto',
  package='autotrade',
  serialized_pb=_b('\n\x0esnapshot.proto\x12\tautotrade\"\xba\x07\n\x06\x66uture\x12\x13\n\x0btrading_day\x18\x01 \x02(\t\x12\x15\n\rinstrument_id\x18\x02 \x02(\t\x12\x13\n\x0b\x65xchange_id\x18\x03 \x01(\t\x12\x18\n\x10\x65xchange_inst_id\x18\x04 \x01(\t\x12\x12\n\nlast_price\x18\x05 \x02(\x02\x12\x1b\n\x13presettlement_price\x18\x06 \x01(\x02\x12\x10\n\x08preclose\x18\x07 \x01(\x02\x12\x18\n\x10preopen_interest\x18\x08 \x01(\x02\x12\x0c\n\x04open\x18\t \x01(\x02\x12\r\n\x05\x63lose\x18\n \x01(\x02\x12\x0c\n\x04high\x18\x0b \x01(\x02\x12\x0b\n\x03low\x18\x0c \x01(\x02\x12\x0e\n\x06volume\x18\r \x02(\x04\x12\x0e\n\x06\x61mount\x18\x0e \x01(\x02\x12\x15\n\ropen_interest\x18\x0f \x01(\x02\x12\x18\n\x10settlement_price\x18\x10 \x01(\x02\x12\x18\n\x10upperlimit_price\x18\x11 \x01(\x02\x12\x18\n\x10lowerlimit_price\x18\x12 \x01(\x02\x12\x11\n\tpre_delta\x18\x13 \x01(\x02\x12\x12\n\ncurr_delta\x18\x14 \x01(\x02\x12\x13\n\x0bupdate_time\x18\x15 \x01(\t\x12\x17\n\x0fupdate_millisec\x18\x16 \x01(\r\x12\x0b\n\x03\x62p1\x18\x17 \x02(\x02\x12\x0b\n\x03\x62p2\x18\x18 \x01(\x02\x12\x0b\n\x03\x62p3\x18\x19 \x01(\x02\x12\x0b\n\x03\x62p4\x18\x1a \x01(\x02\x12\x0b\n\x03\x62p5\x18\x1b \x01(\x02\x12\x0b\n\x03\x62v1\x18\x1c \x02(\r\x12\x0b\n\x03\x62v2\x18\x1d \x01(\r\x12\x0b\n\x03\x62v3\x18\x1e \x01(\r\x12\x0b\n\x03\x62v4\x18\x1f \x01(\r\x12\x0b\n\x03\x62v5\x18  \x01(\r\x12\x0b\n\x03\x61p1\x18! \x02(\x02\x12\x0b\n\x03\x61p2\x18\" \x01(\x02\x12\x0b\n\x03\x61p3\x18# \x01(\x02\x12\x0b\n\x03\x61p4\x18$ \x01(\x02\x12\x0b\n\x03\x61p5\x18% \x01(\x02\x12\x0b\n\x03\x61v1\x18& \x02(\r\x12\x0b\n\x03\x61v2\x18\' \x01(\r\x12\x0b\n\x03\x61v3\x18( \x01(\r\x12\x0b\n\x03\x61v4\x18) \x01(\r\x12\x0b\n\x03\x61v5\x18* \x01(\r\x12\x15\n\raverage_price\x18+ \x01(\x02\x12\x12\n\naction_day\x18, \x01(\t\x12\x0c\n\x04type\x18- \x01(\t\x12\x10\n\x08\x64\x61tetime\x18. \x01(\t\x12\x11\n\tsum_price\x18/ \x01(\x02\x12\x12\n\nnew_volume\x18\x30 \x01(\x05\x12\x16\n\x0etotal_position\x18\x31 \x01(\x05\x12\x17\n\x0fposition_change\x18\x32 \x01(\x05\x12\x13\n\x0bpreposition\x18\x33 \x01(\x02\x12\x15\n\rbought_volume\x18\x34 \x01(\x02\x12\x13\n\x0bsold_volume\x18\x35 \x01(\x02\"\xa6\x01\n\x0e\x66uture_min_bar\x12\x15\n\rinstrument_id\x18\x01 \x02(\t\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\x12\x0c\n\x04open\x18\x04 \x01(\x02\x12\r\n\x05\x63lose\x18\x05 \x01(\x02\x12\x0c\n\x04high\x18\x06 \x01(\x02\x12\x0b\n\x03low\x18\x07 \x01(\x02\x12\x0e\n\x06volume\x18\x08 \x02(\x04\x12\x0e\n\x06\x61mount\x18\t \x01(\x02\x42\nB\x08snapshot')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FUTURE = _descriptor.Descriptor(
  name='future',
  full_name='autotrade.future',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trading_day', full_name='autotrade.future.trading_day', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument_id', full_name='autotrade.future.instrument_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange_id', full_name='autotrade.future.exchange_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange_inst_id', full_name='autotrade.future.exchange_inst_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_price', full_name='autotrade.future.last_price', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presettlement_price', full_name='autotrade.future.presettlement_price', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preclose', full_name='autotrade.future.preclose', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preopen_interest', full_name='autotrade.future.preopen_interest', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='autotrade.future.open', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='autotrade.future.close', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='autotrade.future.high', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='autotrade.future.low', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='autotrade.future.volume', index=12,
      number=13, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='autotrade.future.amount', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_interest', full_name='autotrade.future.open_interest', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settlement_price', full_name='autotrade.future.settlement_price', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upperlimit_price', full_name='autotrade.future.upperlimit_price', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowerlimit_price', full_name='autotrade.future.lowerlimit_price', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_delta', full_name='autotrade.future.pre_delta', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curr_delta', full_name='autotrade.future.curr_delta', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='autotrade.future.update_time', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_millisec', full_name='autotrade.future.update_millisec', index=21,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp1', full_name='autotrade.future.bp1', index=22,
      number=23, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp2', full_name='autotrade.future.bp2', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp3', full_name='autotrade.future.bp3', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp4', full_name='autotrade.future.bp4', index=25,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bp5', full_name='autotrade.future.bp5', index=26,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bv1', full_name='autotrade.future.bv1', index=27,
      number=28, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bv2', full_name='autotrade.future.bv2', index=28,
      number=29, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bv3', full_name='autotrade.future.bv3', index=29,
      number=30, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bv4', full_name='autotrade.future.bv4', index=30,
      number=31, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bv5', full_name='autotrade.future.bv5', index=31,
      number=32, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap1', full_name='autotrade.future.ap1', index=32,
      number=33, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap2', full_name='autotrade.future.ap2', index=33,
      number=34, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap3', full_name='autotrade.future.ap3', index=34,
      number=35, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap4', full_name='autotrade.future.ap4', index=35,
      number=36, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap5', full_name='autotrade.future.ap5', index=36,
      number=37, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='av1', full_name='autotrade.future.av1', index=37,
      number=38, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='av2', full_name='autotrade.future.av2', index=38,
      number=39, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='av3', full_name='autotrade.future.av3', index=39,
      number=40, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='av4', full_name='autotrade.future.av4', index=40,
      number=41, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='av5', full_name='autotrade.future.av5', index=41,
      number=42, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_price', full_name='autotrade.future.average_price', index=42,
      number=43, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_day', full_name='autotrade.future.action_day', index=43,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='autotrade.future.type', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='autotrade.future.datetime', index=45,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sum_price', full_name='autotrade.future.sum_price', index=46,
      number=47, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_volume', full_name='autotrade.future.new_volume', index=47,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_position', full_name='autotrade.future.total_position', index=48,
      number=49, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position_change', full_name='autotrade.future.position_change', index=49,
      number=50, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preposition', full_name='autotrade.future.preposition', index=50,
      number=51, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bought_volume', full_name='autotrade.future.bought_volume', index=51,
      number=52, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sold_volume', full_name='autotrade.future.sold_volume', index=52,
      number=53, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=984,
)


_FUTURE_MIN_BAR = _descriptor.Descriptor(
  name='future_min_bar',
  full_name='autotrade.future_min_bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument_id', full_name='autotrade.future_min_bar.instrument_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange_id', full_name='autotrade.future_min_bar.exchange_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='autotrade.future_min_bar.datetime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='autotrade.future_min_bar.open', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='autotrade.future_min_bar.close', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='autotrade.future_min_bar.high', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='autotrade.future_min_bar.low', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='autotrade.future_min_bar.volume', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='autotrade.future_min_bar.amount', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=987,
  serialized_end=1153,
)

DESCRIPTOR.message_types_by_name['future'] = _FUTURE
DESCRIPTOR.message_types_by_name['future_min_bar'] = _FUTURE_MIN_BAR

future = _reflection.GeneratedProtocolMessageType('future', (_message.Message,), dict(
  DESCRIPTOR = _FUTURE,
  __module__ = 'snapshot_pb2'
  # @@protoc_insertion_point(class_scope:autotrade.future)
  ))
_sym_db.RegisterMessage(future)

future_min_bar = _reflection.GeneratedProtocolMessageType('future_min_bar', (_message.Message,), dict(
  DESCRIPTOR = _FUTURE_MIN_BAR,
  __module__ = 'snapshot_pb2'
  # @@protoc_insertion_point(class_scope:autotrade.future_min_bar)
  ))
_sym_db.RegisterMessage(future_min_bar)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\010snapshot'))
# @@protoc_insertion_point(module_scope)
