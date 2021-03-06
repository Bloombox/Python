# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/stats/SessionStats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bq_field_pb2 as bq__field__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/stats/SessionStats.proto',
  package='bloombox.schema.analytics.stats',
  syntax='proto3',
  serialized_pb=_b('\n\"analytics/stats/SessionStats.proto\x12\x1f\x62loombox.schema.analytics.stats\x1a\x0e\x62q_field.proto\x1a\x16temporal/Instant.proto\"\xc8\x04\n\x0cSessionStats\x12.\n\x03sid\x18\x01 \x01(\tB!\xf0?\x01\x8a@\x1bOriginal ID of the session.\x12P\n\rpartner_scope\x18\x02 \x01(\tB9\xf0?\x01\x8a@3Partner scope seen as associated with this session.\x12\x46\n\x0b\x65vent_count\x18\x03 \x01(\rB1\xf0?\x01\x8a@+Count of total events seen in this session.\x12q\n\x05\x62\x65gin\x18\x04 \x01(\x0b\x32\x1e.opencannabis.temporal.InstantBB\xf0?\x01\x8a@<Timestamp representing the first event seen in this session.\x12n\n\x03\x65nd\x18\x05 \x01(\x0b\x32\x1e.opencannabis.temporal.InstantBA\xf0?\x01\x8a@;Timestamp representing the last event seen in this session.\x12H\n\tdevice_id\x18\x06 \x01(\tB5\xf0?\x01\x8a@/Device ID seen as associated with this session.\x12\x41\n\x07user_id\x18\x07 \x01(\tB0\x8a@-User ID seen as associated with this session.B@\n\"io.bloombox.schema.telemetry.statsB\x10SessionTelemetryH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,])




_SESSIONSTATS = _descriptor.Descriptor(
  name='SessionStats',
  full_name='bloombox.schema.analytics.stats.SessionStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='bloombox.schema.analytics.stats.SessionStats.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\033Original ID of the session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_scope', full_name='bloombox.schema.analytics.stats.SessionStats.partner_scope', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@3Partner scope seen as associated with this session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_count', full_name='bloombox.schema.analytics.stats.SessionStats.event_count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@+Count of total events seen in this session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin', full_name='bloombox.schema.analytics.stats.SessionStats.begin', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@<Timestamp representing the first event seen in this session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='bloombox.schema.analytics.stats.SessionStats.end', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@;Timestamp representing the last event seen in this session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='bloombox.schema.analytics.stats.SessionStats.device_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@/Device ID seen as associated with this session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='bloombox.schema.analytics.stats.SessionStats.user_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-User ID seen as associated with this session.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=696,
)

_SESSIONSTATS.fields_by_name['begin'].message_type = temporal_dot_Instant__pb2._INSTANT
_SESSIONSTATS.fields_by_name['end'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['SessionStats'] = _SESSIONSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionStats = _reflection.GeneratedProtocolMessageType('SessionStats', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONSTATS,
  __module__ = 'analytics.stats.SessionStats_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.stats.SessionStats)
  ))
_sym_db.RegisterMessage(SessionStats)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"io.bloombox.schema.telemetry.statsB\020SessionTelemetryH\001P\000\242\002\003BBS'))
_SESSIONSTATS.fields_by_name['sid'].has_options = True
_SESSIONSTATS.fields_by_name['sid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\033Original ID of the session.'))
_SESSIONSTATS.fields_by_name['partner_scope'].has_options = True
_SESSIONSTATS.fields_by_name['partner_scope']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@3Partner scope seen as associated with this session.'))
_SESSIONSTATS.fields_by_name['event_count'].has_options = True
_SESSIONSTATS.fields_by_name['event_count']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@+Count of total events seen in this session.'))
_SESSIONSTATS.fields_by_name['begin'].has_options = True
_SESSIONSTATS.fields_by_name['begin']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@<Timestamp representing the first event seen in this session.'))
_SESSIONSTATS.fields_by_name['end'].has_options = True
_SESSIONSTATS.fields_by_name['end']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@;Timestamp representing the last event seen in this session.'))
_SESSIONSTATS.fields_by_name['device_id'].has_options = True
_SESSIONSTATS.fields_by_name['device_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@/Device ID seen as associated with this session.'))
_SESSIONSTATS.fields_by_name['user_id'].has_options = True
_SESSIONSTATS.fields_by_name['user_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-User ID seen as associated with this session.'))
# @@protoc_insertion_point(module_scope)
