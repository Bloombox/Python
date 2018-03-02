# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/v1beta1/AuthService_Beta1.proto

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


from identity import User_pb2 as identity_dot_User__pb2
from services import ServiceStatus_pb2 as services_dot_ServiceStatus__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth/v1beta1/AuthService_Beta1.proto',
  package='bloombox.schema.services.auth.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n$auth/v1beta1/AuthService_Beta1.proto\x12%bloombox.schema.services.auth.v1beta1\x1a\x13identity/User.proto\x1a\x1cservices/ServiceStatus.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\x01\n\x04Ping\x1a\t\n\x07Request\x1a\x43\n\x08Response\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.bloombox.schema.services.ServiceStatus\x1a\x99\x01\n\tOperation\x12\x44\n\x07request\x18\x01 \x01(\x0b\x32\x33.bloombox.schema.services.auth.v1beta1.Ping.Request\x12\x46\n\x08response\x18\x02 \x01(\x0b\x32\x34.bloombox.schema.services.auth.v1beta1.Ping.Response\"9\n\x16\x45mailPasswordAssertion\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x16\x46irebaseTokenAssertion\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\"\xcb\x01\n\x10\x41\x63\x63ountAssertion\x12W\n\x0e\x65mail_password\x18\x01 \x01(\x0b\x32=.bloombox.schema.services.auth.v1beta1.EmailPasswordAssertionH\x00\x12Q\n\x08\x66irebase\x18\x02 \x01(\x0b\x32=.bloombox.schema.services.auth.v1beta1.FirebaseTokenAssertionH\x00\x42\x0b\n\tassertion\"\xd4\x03\n\x10\x41uthenticateUser\x1a\x93\x01\n\x07Request\x12<\n\x08provider\x18\x01 \x01(\x0e\x32*.bloombox.schema.identity.IdentityProvider\x12J\n\tassertion\x18\x02 \x01(\x0b\x32\x37.bloombox.schema.services.auth.v1beta1.AccountAssertion\x1av\n\x08Response\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32\x31.bloombox.schema.services.auth.v1beta1.AuthStatus\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\x1a\xb1\x01\n\tOperation\x12P\n\x07request\x18\x01 \x01(\x0b\x32?.bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request\x12R\n\x08response\x18\x02 \x01(\x0b\x32@.bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response*\x19\n\tAuthError\x12\x0c\n\x08NO_ERROR\x10\x00*W\n\nAuthStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0e\x41\x43\x43\x45SS_GRANTED\x10\x01\x12\x11\n\rACCESS_DENIED\x10\x02\x12\x15\n\x11\x41\x43\x43OUNT_SUSPENDED\x10\x03\x32\xdd\x02\n\x04\x41uth\x12\x8d\x01\n\x04Ping\x12\x33.bloombox.schema.services.auth.v1beta1.Ping.Request\x1a\x34.bloombox.schema.services.auth.v1beta1.Ping.Response\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/auth/v1beta1/ping\x12\xc4\x01\n\x0c\x41uthenticate\x12?.bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request\x1a@.bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response\"1\x82\xd3\xe4\x93\x02+\"\x1e/auth/v1beta1/login/{provider}:\tassertionB4\n(io.bloombox.schema.services.auth.v1beta1H\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[identity_dot_User__pb2.DESCRIPTOR,services_dot_ServiceStatus__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_AUTHERROR = _descriptor.EnumDescriptor(
  name='AuthError',
  full_name='bloombox.schema.services.auth.v1beta1.AuthError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1195,
  serialized_end=1220,
)
_sym_db.RegisterEnumDescriptor(_AUTHERROR)

AuthError = enum_type_wrapper.EnumTypeWrapper(_AUTHERROR)
_AUTHSTATUS = _descriptor.EnumDescriptor(
  name='AuthStatus',
  full_name='bloombox.schema.services.auth.v1beta1.AuthStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_GRANTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_SUSPENDED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1222,
  serialized_end=1309,
)
_sym_db.RegisterEnumDescriptor(_AUTHSTATUS)

AuthStatus = enum_type_wrapper.EnumTypeWrapper(_AUTHSTATUS)
NO_ERROR = 0
UNKNOWN = 0
ACCESS_GRANTED = 1
ACCESS_DENIED = 2
ACCOUNT_SUSPENDED = 3



_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.auth.v1beta1.Ping.Request',
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
  serialized_start=169,
  serialized_end=178,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.auth.v1beta1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.auth.v1beta1.Ping.Response.status', index=0,
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
  serialized_start=180,
  serialized_end=247,
)

_PING_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.auth.v1beta1.Ping.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.auth.v1beta1.Ping.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.auth.v1beta1.Ping.Operation.response', index=1,
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
  serialized_start=250,
  serialized_end=403,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.auth.v1beta1.Ping',
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
  serialized_start=161,
  serialized_end=403,
)


_EMAILPASSWORDASSERTION = _descriptor.Descriptor(
  name='EmailPasswordAssertion',
  full_name='bloombox.schema.services.auth.v1beta1.EmailPasswordAssertion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='bloombox.schema.services.auth.v1beta1.EmailPasswordAssertion.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='bloombox.schema.services.auth.v1beta1.EmailPasswordAssertion.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=405,
  serialized_end=462,
)


_FIREBASETOKENASSERTION = _descriptor.Descriptor(
  name='FirebaseTokenAssertion',
  full_name='bloombox.schema.services.auth.v1beta1.FirebaseTokenAssertion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='bloombox.schema.services.auth.v1beta1.FirebaseTokenAssertion.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='bloombox.schema.services.auth.v1beta1.FirebaseTokenAssertion.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=464,
  serialized_end=516,
)


_ACCOUNTASSERTION = _descriptor.Descriptor(
  name='AccountAssertion',
  full_name='bloombox.schema.services.auth.v1beta1.AccountAssertion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email_password', full_name='bloombox.schema.services.auth.v1beta1.AccountAssertion.email_password', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firebase', full_name='bloombox.schema.services.auth.v1beta1.AccountAssertion.firebase', index=1,
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
    _descriptor.OneofDescriptor(
      name='assertion', full_name='bloombox.schema.services.auth.v1beta1.AccountAssertion.assertion',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=519,
  serialized_end=722,
)


_AUTHENTICATEUSER_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request.provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assertion', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request.assertion', index=1,
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
  serialized_start=746,
  serialized_end=893,
)

_AUTHENTICATEUSER_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=895,
  serialized_end=1013,
)

_AUTHENTICATEUSER_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser.Operation.response', index=1,
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
  serialized_start=1016,
  serialized_end=1193,
)

_AUTHENTICATEUSER = _descriptor.Descriptor(
  name='AuthenticateUser',
  full_name='bloombox.schema.services.auth.v1beta1.AuthenticateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_AUTHENTICATEUSER_REQUEST, _AUTHENTICATEUSER_RESPONSE, _AUTHENTICATEUSER_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=1193,
)

_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = services_dot_ServiceStatus__pb2._SERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_PING_OPERATION.fields_by_name['request'].message_type = _PING_REQUEST
_PING_OPERATION.fields_by_name['response'].message_type = _PING_RESPONSE
_PING_OPERATION.containing_type = _PING
_ACCOUNTASSERTION.fields_by_name['email_password'].message_type = _EMAILPASSWORDASSERTION
_ACCOUNTASSERTION.fields_by_name['firebase'].message_type = _FIREBASETOKENASSERTION
_ACCOUNTASSERTION.oneofs_by_name['assertion'].fields.append(
  _ACCOUNTASSERTION.fields_by_name['email_password'])
_ACCOUNTASSERTION.fields_by_name['email_password'].containing_oneof = _ACCOUNTASSERTION.oneofs_by_name['assertion']
_ACCOUNTASSERTION.oneofs_by_name['assertion'].fields.append(
  _ACCOUNTASSERTION.fields_by_name['firebase'])
_ACCOUNTASSERTION.fields_by_name['firebase'].containing_oneof = _ACCOUNTASSERTION.oneofs_by_name['assertion']
_AUTHENTICATEUSER_REQUEST.fields_by_name['provider'].enum_type = identity_dot_User__pb2._IDENTITYPROVIDER
_AUTHENTICATEUSER_REQUEST.fields_by_name['assertion'].message_type = _ACCOUNTASSERTION
_AUTHENTICATEUSER_REQUEST.containing_type = _AUTHENTICATEUSER
_AUTHENTICATEUSER_RESPONSE.fields_by_name['status'].enum_type = _AUTHSTATUS
_AUTHENTICATEUSER_RESPONSE.containing_type = _AUTHENTICATEUSER
_AUTHENTICATEUSER_OPERATION.fields_by_name['request'].message_type = _AUTHENTICATEUSER_REQUEST
_AUTHENTICATEUSER_OPERATION.fields_by_name['response'].message_type = _AUTHENTICATEUSER_RESPONSE
_AUTHENTICATEUSER_OPERATION.containing_type = _AUTHENTICATEUSER
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['EmailPasswordAssertion'] = _EMAILPASSWORDASSERTION
DESCRIPTOR.message_types_by_name['FirebaseTokenAssertion'] = _FIREBASETOKENASSERTION
DESCRIPTOR.message_types_by_name['AccountAssertion'] = _ACCOUNTASSERTION
DESCRIPTOR.message_types_by_name['AuthenticateUser'] = _AUTHENTICATEUSER
DESCRIPTOR.enum_types_by_name['AuthError'] = _AUTHERROR
DESCRIPTOR.enum_types_by_name['AuthStatus'] = _AUTHSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.Ping.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PING_OPERATION,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.Ping.Operation)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)
_sym_db.RegisterMessage(Ping.Operation)

EmailPasswordAssertion = _reflection.GeneratedProtocolMessageType('EmailPasswordAssertion', (_message.Message,), dict(
  DESCRIPTOR = _EMAILPASSWORDASSERTION,
  __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.EmailPasswordAssertion)
  ))
_sym_db.RegisterMessage(EmailPasswordAssertion)

FirebaseTokenAssertion = _reflection.GeneratedProtocolMessageType('FirebaseTokenAssertion', (_message.Message,), dict(
  DESCRIPTOR = _FIREBASETOKENASSERTION,
  __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.FirebaseTokenAssertion)
  ))
_sym_db.RegisterMessage(FirebaseTokenAssertion)

AccountAssertion = _reflection.GeneratedProtocolMessageType('AccountAssertion', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTASSERTION,
  __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.AccountAssertion)
  ))
_sym_db.RegisterMessage(AccountAssertion)

AuthenticateUser = _reflection.GeneratedProtocolMessageType('AuthenticateUser', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _AUTHENTICATEUSER_REQUEST,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.AuthenticateUser.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _AUTHENTICATEUSER_RESPONSE,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.AuthenticateUser.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _AUTHENTICATEUSER_OPERATION,
    __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.AuthenticateUser.Operation)
    ))
  ,
  DESCRIPTOR = _AUTHENTICATEUSER,
  __module__ = 'auth.v1beta1.AuthService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.auth.v1beta1.AuthenticateUser)
  ))
_sym_db.RegisterMessage(AuthenticateUser)
_sym_db.RegisterMessage(AuthenticateUser.Request)
_sym_db.RegisterMessage(AuthenticateUser.Response)
_sym_db.RegisterMessage(AuthenticateUser.Operation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n(io.bloombox.schema.services.auth.v1beta1H\001P\001\242\002\003BBS'))

_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='bloombox.schema.services.auth.v1beta1.Auth',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1312,
  serialized_end=1661,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.auth.v1beta1.Auth.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\024\022\022/auth/v1beta1/ping')),
  ),
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='bloombox.schema.services.auth.v1beta1.Auth.Authenticate',
    index=1,
    containing_service=None,
    input_type=_AUTHENTICATEUSER_REQUEST,
    output_type=_AUTHENTICATEUSER_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002+\"\036/auth/v1beta1/login/{provider}:\tassertion')),
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)