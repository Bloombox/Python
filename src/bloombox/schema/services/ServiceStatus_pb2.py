# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/ServiceStatus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/ServiceStatus.proto',
  package='bloombox.schema.services',
  syntax='proto3',
  serialized_pb=_b('\n\x1cservices/ServiceStatus.proto\x12\x18\x62loombox.schema.services*?\n\rServiceStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04\x44OWN\x10\x02\x12\x0f\n\x0bMAINTENANCE\x10\x03\x42\'\n\x1bio.bloombox.schema.servicesH\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
)

_SERVICESTATUS = _descriptor.EnumDescriptor(
  name='ServiceStatus',
  full_name='bloombox.schema.services.ServiceStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAINTENANCE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=58,
  serialized_end=121,
)
_sym_db.RegisterEnumDescriptor(_SERVICESTATUS)

ServiceStatus = enum_type_wrapper.EnumTypeWrapper(_SERVICESTATUS)
UNKNOWN = 0
UP = 1
DOWN = 2
MAINTENANCE = 3


DESCRIPTOR.enum_types_by_name['ServiceStatus'] = _SERVICESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.bloombox.schema.servicesH\001P\001\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
