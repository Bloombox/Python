# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pos/v1beta1/POSService_Beta1.proto

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


from services import ServiceStatus_pb2 as services_dot_ServiceStatus__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pos/v1beta1/POSService_Beta1.proto',
  package='bloombox.schema.services.pos.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\"pos/v1beta1/POSService_Beta1.proto\x12$bloombox.schema.services.pos.v1beta1\x1a\x1cservices/ServiceStatus.proto\x1a\x1cgoogle/api/annotations.proto\"\xf0\x01\n\x04Ping\x1a\t\n\x07Request\x1a\x43\n\x08Response\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.bloombox.schema.services.ServiceStatus\x1a\x97\x01\n\tOperation\x12\x43\n\x07request\x18\x01 \x01(\x0b\x32\x32.bloombox.schema.services.pos.v1beta1.Ping.Request\x12\x45\n\x08response\x18\x02 \x01(\x0b\x32\x33.bloombox.schema.services.pos.v1beta1.Ping.Response*\xb2\x01\n\x08POSError\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12INVALID_COLLECTION\x10\x01\x12\x13\n\x0fINVALID_PARTNER\x10\x02\x12\x14\n\x10INVALID_LOCATION\x10\x03\x12\x12\n\x0eINVALID_DEVICE\x10\x04\x12\x15\n\x11PARTNER_NOT_FOUND\x10\x05\x12\x16\n\x12LOCATION_NOT_FOUND\x10\x06\x12\x13\n\x0fINVALID_PAYLOAD\x10\x63\x32\x96\x01\n\x0bPointOfSale\x12\x86\x01\n\x04Ping\x12\x32.bloombox.schema.services.pos.v1beta1.Ping.Request\x1a\x33.bloombox.schema.services.pos.v1beta1.Ping.Response\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1beta1/pingB3\n\'io.bloombox.schema.services.pos.v1beta1H\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[services_dot_ServiceStatus__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_POSERROR = _descriptor.EnumDescriptor(
  name='POSError',
  full_name='bloombox.schema.services.pos.v1beta1.POSError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COLLECTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARTNER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LOCATION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEVICE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_NOT_FOUND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_NOT_FOUND', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAYLOAD', index=7, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=380,
  serialized_end=558,
)
_sym_db.RegisterEnumDescriptor(_POSERROR)

POSError = enum_type_wrapper.EnumTypeWrapper(_POSERROR)
UNKNOWN = 0
INVALID_COLLECTION = 1
INVALID_PARTNER = 2
INVALID_LOCATION = 3
INVALID_DEVICE = 4
PARTNER_NOT_FOUND = 5
LOCATION_NOT_FOUND = 6
INVALID_PAYLOAD = 99



_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.pos.v1beta1.Ping.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=145,
  serialized_end=154,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.pos.v1beta1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.pos.v1beta1.Ping.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=156,
  serialized_end=223,
)

_PING_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.pos.v1beta1.Ping.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.pos.v1beta1.Ping.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.pos.v1beta1.Ping.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=226,
  serialized_end=377,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.pos.v1beta1.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PING_REQUEST, _PING_RESPONSE, _PING_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=377,
)

_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = services_dot_ServiceStatus__pb2._SERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_PING_OPERATION.fields_by_name['request'].message_type = _PING_REQUEST
_PING_OPERATION.fields_by_name['response'].message_type = _PING_RESPONSE
_PING_OPERATION.containing_type = _PING
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.enum_types_by_name['POSError'] = _POSERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'pos.v1beta1.POSService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.pos.v1beta1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'pos.v1beta1.POSService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.pos.v1beta1.Ping.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PING_OPERATION,
    __module__ = 'pos.v1beta1.POSService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.pos.v1beta1.Ping.Operation)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'pos.v1beta1.POSService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.pos.v1beta1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)
_sym_db.RegisterMessage(Ping.Operation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'io.bloombox.schema.services.pos.v1beta1H\001P\001\242\002\003BBS'))

_POINTOFSALE = _descriptor.ServiceDescriptor(
  name='PointOfSale',
  full_name='bloombox.schema.services.pos.v1beta1.PointOfSale',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=561,
  serialized_end=711,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.pos.v1beta1.PointOfSale.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\017\022\r/v1beta1/ping')),
  ),
])
_sym_db.RegisterServiceDescriptor(_POINTOFSALE)

DESCRIPTOR.services_by_name['PointOfSale'] = _POINTOFSALE

# @@protoc_insertion_point(module_scope)
