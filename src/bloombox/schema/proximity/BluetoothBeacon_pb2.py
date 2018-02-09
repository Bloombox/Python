# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proximity/BluetoothBeacon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from geo import Location_pb2 as geo_dot_Location__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proximity/BluetoothBeacon.proto',
  package='opencannabis.proximity',
  syntax='proto3',
  serialized_pb=_b('\n\x1fproximity/BluetoothBeacon.proto\x12\x16opencannabis.proximity\x1a\x12geo/Location.proto\x1a\x16temporal/Instant.proto\"\xcf\x01\n\x0f\x42luetoothBeacon\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05major\x18\x02 \x01(\r\x12\r\n\x05minor\x18\x03 \x01(\r\x12,\n\x04seen\x18\x04 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\x12,\n\x08location\x18\x05 \x01(\x0b\x32\x1a.opencannabis.geo.Location\x12\x34\n\x08\x61\x63\x63uracy\x18\x06 \x01(\x0b\x32\".opencannabis.geo.LocationAccuracyB,\n io.opencannabis.schema.proximityH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[geo_dot_Location__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,])




_BLUETOOTHBEACON = _descriptor.Descriptor(
  name='BluetoothBeacon',
  full_name='opencannabis.proximity.BluetoothBeacon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='opencannabis.proximity.BluetoothBeacon.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='major', full_name='opencannabis.proximity.BluetoothBeacon.major', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='opencannabis.proximity.BluetoothBeacon.minor', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seen', full_name='opencannabis.proximity.BluetoothBeacon.seen', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='opencannabis.proximity.BluetoothBeacon.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='opencannabis.proximity.BluetoothBeacon.accuracy', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=104,
  serialized_end=311,
)

_BLUETOOTHBEACON.fields_by_name['seen'].message_type = temporal_dot_Instant__pb2._INSTANT
_BLUETOOTHBEACON.fields_by_name['location'].message_type = geo_dot_Location__pb2._LOCATION
_BLUETOOTHBEACON.fields_by_name['accuracy'].message_type = geo_dot_Location__pb2._LOCATIONACCURACY
DESCRIPTOR.message_types_by_name['BluetoothBeacon'] = _BLUETOOTHBEACON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BluetoothBeacon = _reflection.GeneratedProtocolMessageType('BluetoothBeacon', (_message.Message,), dict(
  DESCRIPTOR = _BLUETOOTHBEACON,
  __module__ = 'proximity.BluetoothBeacon_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.proximity.BluetoothBeacon)
  ))
_sym_db.RegisterMessage(BluetoothBeacon)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n io.opencannabis.schema.proximityH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
