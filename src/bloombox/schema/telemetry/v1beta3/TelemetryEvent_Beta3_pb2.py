# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry/v1beta3/TelemetryEvent_Beta3.proto

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
from analytics import Context_pb2 as analytics_dot_Context__pb2
from analytics.generic import Event_pb2 as analytics_dot_generic_dot_Event__pb2
from analytics.generic import Exception_pb2 as analytics_dot_generic_dot_Exception__pb2
from telemetry.v1beta3 import TelemetryService_Beta3_pb2 as telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry/v1beta3/TelemetryEvent_Beta3.proto',
  package='bloombox.schema.services.telemetry.v1beta3',
  syntax='proto3',
  serialized_pb=_b('\n,telemetry/v1beta3/TelemetryEvent_Beta3.proto\x12*bloombox.schema.services.telemetry.v1beta3\x1a\x0e\x62q_field.proto\x1a\x17\x61nalytics/Context.proto\x1a\x1d\x61nalytics/generic/Event.proto\x1a!analytics/generic/Exception.proto\x1a.telemetry/v1beta3/TelemetryService_Beta3.proto\"\xcb\x05\n\x0eTelemetryEvent\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x10\n\x08internal\x18\x03 \x01(\x08\x12\x38\n\x06timing\x18\x04 \x01(\x0b\x32(.bloombox.schema.analytics.EventPosition\x12\x33\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\".bloombox.schema.analytics.Context\x12\x36\n\x06\x61\x63tors\x18\x06 \x01(\x0b\x32&.bloombox.schema.analytics.EventActors\x12;\n\x07generic\x18\n \x01(\x0b\x32(.bloombox.schema.analytics.generic.EventH\x00\x12=\n\x05\x65rror\x18\x0b \x01(\x0b\x32,.bloombox.schema.analytics.generic.ExceptionH\x00\x12\\\n\nimpression\x18\x14 \x01(\x0b\x32\x46.bloombox.schema.services.telemetry.v1beta3.CommercialEvent.ImpressionH\x00\x12P\n\x04view\x18\x15 \x01(\x0b\x32@.bloombox.schema.services.telemetry.v1beta3.CommercialEvent.ViewH\x00\x12T\n\x06\x61\x63tion\x18\x16 \x01(\x0b\x32\x42.bloombox.schema.services.telemetry.v1beta3.CommercialEvent.ActionH\x00\x12W\n\x0buser_action\x18\x1e \x01(\x0b\x32@.bloombox.schema.services.telemetry.v1beta3.IdentityEvent.ActionH\x00\x42\x07\n\x05\x65ventBc\n-io.bloombox.schema.services.telemetry.v1beta3B\x11\x41nalyticsPipelineH\x01P\x00\xf8\x01\x01\xa2\x02\x03\x42\x42S\xaa\x02\x11Telemetry.v1beta3b\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,analytics_dot_Context__pb2.DESCRIPTOR,analytics_dot_generic_dot_Event__pb2.DESCRIPTOR,analytics_dot_generic_dot_Exception__pb2.DESCRIPTOR,telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2.DESCRIPTOR,])




_TELEMETRYEVENT = _descriptor.Descriptor(
  name='TelemetryEvent',
  full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.parent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.internal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.timing', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actors', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.actors', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generic', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.generic', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.error', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impression', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.impression', index=8,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.view', index=9,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.action', index=10,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_action', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.user_action', index=11,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='event', full_name='bloombox.schema.services.telemetry.v1beta3.TelemetryEvent.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=248,
  serialized_end=963,
)

_TELEMETRYEVENT.fields_by_name['timing'].message_type = analytics_dot_Context__pb2._EVENTPOSITION
_TELEMETRYEVENT.fields_by_name['context'].message_type = analytics_dot_Context__pb2._CONTEXT
_TELEMETRYEVENT.fields_by_name['actors'].message_type = analytics_dot_Context__pb2._EVENTACTORS
_TELEMETRYEVENT.fields_by_name['generic'].message_type = analytics_dot_generic_dot_Event__pb2._EVENT
_TELEMETRYEVENT.fields_by_name['error'].message_type = analytics_dot_generic_dot_Exception__pb2._EXCEPTION
_TELEMETRYEVENT.fields_by_name['impression'].message_type = telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2._COMMERCIALEVENT_IMPRESSION
_TELEMETRYEVENT.fields_by_name['view'].message_type = telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2._COMMERCIALEVENT_VIEW
_TELEMETRYEVENT.fields_by_name['action'].message_type = telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2._COMMERCIALEVENT_ACTION
_TELEMETRYEVENT.fields_by_name['user_action'].message_type = telemetry_dot_v1beta3_dot_TelemetryService__Beta3__pb2._IDENTITYEVENT_ACTION
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['generic'])
_TELEMETRYEVENT.fields_by_name['generic'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['error'])
_TELEMETRYEVENT.fields_by_name['error'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['impression'])
_TELEMETRYEVENT.fields_by_name['impression'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['view'])
_TELEMETRYEVENT.fields_by_name['view'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['action'])
_TELEMETRYEVENT.fields_by_name['action'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
_TELEMETRYEVENT.oneofs_by_name['event'].fields.append(
  _TELEMETRYEVENT.fields_by_name['user_action'])
_TELEMETRYEVENT.fields_by_name['user_action'].containing_oneof = _TELEMETRYEVENT.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['TelemetryEvent'] = _TELEMETRYEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelemetryEvent = _reflection.GeneratedProtocolMessageType('TelemetryEvent', (_message.Message,), dict(
  DESCRIPTOR = _TELEMETRYEVENT,
  __module__ = 'telemetry.v1beta3.TelemetryEvent_Beta3_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.telemetry.v1beta3.TelemetryEvent)
  ))
_sym_db.RegisterMessage(TelemetryEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n-io.bloombox.schema.services.telemetry.v1beta3B\021AnalyticsPipelineH\001P\000\370\001\001\242\002\003BBS\252\002\021Telemetry.v1beta3'))
# @@protoc_insertion_point(module_scope)
