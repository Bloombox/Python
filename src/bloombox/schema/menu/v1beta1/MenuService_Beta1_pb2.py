# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: menu/v1beta1/MenuService_Beta1.proto

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


from products.menu import Menu_pb2 as products_dot_menu_dot_Menu__pb2
from products.menu import Section_pb2 as products_dot_menu_dot_Section__pb2
from services import ServiceStatus_pb2 as services_dot_ServiceStatus__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='menu/v1beta1/MenuService_Beta1.proto',
  package='bloombox.schema.services.menu.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n$menu/v1beta1/MenuService_Beta1.proto\x12%bloombox.schema.services.menu.v1beta1\x1a\x18products/menu/Menu.proto\x1a\x1bproducts/menu/Section.proto\x1a\x1cservices/ServiceStatus.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\x01\n\x04Ping\x1a\t\n\x07Request\x1a\x43\n\x08Response\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.bloombox.schema.services.ServiceStatus\x1a\x99\x01\n\tOperation\x12\x44\n\x07request\x18\x01 \x01(\x0b\x32\x33.bloombox.schema.services.menu.v1beta1.Ping.Request\x12\x46\n\x08response\x18\x02 \x01(\x0b\x32\x34.bloombox.schema.services.menu.v1beta1.Ping.Response\"\xf8\x01\n\x07GetMenu\x1a\x9e\x01\n\x07Request\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0c\n\x04\x66ull\x18\x02 \x01(\x08\x12\x11\n\tkeys_only\x18\x03 \x01(\x08\x12\x10\n\x08snapshot\x18\x04 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x05 \x01(\t\x12<\n\x07section\x18\x06 \x01(\x0e\x32+.opencannabis.products.menu.section.Section\x1aL\n\x08Response\x12\x31\n\x07\x63\x61talog\x18\x01 \x01(\x0b\x32 .opencannabis.products.menu.Menu\x12\r\n\x05\x63ount\x18\x02 \x01(\x05*\x98\x01\n\tMenuError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x13\n\x0fPARTNER_INVALID\x10\x01\x12\x14\n\x10LOCATION_INVALID\x10\x02\x12\x13\n\x0fSECTION_INVALID\x10\x03\x12\x15\n\x11SECTION_NOT_FOUND\x10\x04\x12\x12\n\x0eMENU_NOT_FOUND\x10\x05\x12\x12\n\x0eINTERNAL_ERROR\x10\x06\x32\x9f\x03\n\x04Menu\x12\x8d\x01\n\x04Ping\x12\x33.bloombox.schema.services.menu.v1beta1.Ping.Request\x1a\x34.bloombox.schema.services.menu.v1beta1.Ping.Response\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/menu/v1beta1/ping\x12\x86\x02\n\x08Retrieve\x12\x36.bloombox.schema.services.menu.v1beta1.GetMenu.Request\x1a\x37.bloombox.schema.services.menu.v1beta1.GetMenu.Response\"\x88\x01\x82\xd3\xe4\x93\x02\x81\x01\x12</menu/v1beta1/{scope=partners/*/locations/*}/global:retrieveZA\x12?/menu/v1beta1/{scope=partners/*/locations/*}/{section}:retrieveB4\n(io.bloombox.schema.services.menu.v1beta1H\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[products_dot_menu_dot_Menu__pb2.DESCRIPTOR,products_dot_menu_dot_Section__pb2.DESCRIPTOR,services_dot_ServiceStatus__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_MENUERROR = _descriptor.EnumDescriptor(
  name='MenuError',
  full_name='bloombox.schema.services.menu.v1beta1.MenuError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_INVALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_INVALID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_INVALID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_NOT_FOUND', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MENU_NOT_FOUND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=691,
  serialized_end=843,
)
_sym_db.RegisterEnumDescriptor(_MENUERROR)

MenuError = enum_type_wrapper.EnumTypeWrapper(_MENUERROR)
NO_ERROR = 0
PARTNER_INVALID = 1
LOCATION_INVALID = 2
SECTION_INVALID = 3
SECTION_NOT_FOUND = 4
MENU_NOT_FOUND = 5
INTERNAL_ERROR = 6



_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.menu.v1beta1.Ping.Request',
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
  serialized_start=203,
  serialized_end=212,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.menu.v1beta1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.menu.v1beta1.Ping.Response.status', index=0,
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
  serialized_start=214,
  serialized_end=281,
)

_PING_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.menu.v1beta1.Ping.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.menu.v1beta1.Ping.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.menu.v1beta1.Ping.Operation.response', index=1,
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
  serialized_start=284,
  serialized_end=437,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.menu.v1beta1.Ping',
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
  serialized_start=195,
  serialized_end=437,
)


_GETMENU_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.full', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys_only', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.keys_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.snapshot', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.fingerprint', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Request.section', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=452,
  serialized_end=610,
)

_GETMENU_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='catalog', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Response.catalog', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='bloombox.schema.services.menu.v1beta1.GetMenu.Response.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=612,
  serialized_end=688,
)

_GETMENU = _descriptor.Descriptor(
  name='GetMenu',
  full_name='bloombox.schema.services.menu.v1beta1.GetMenu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_GETMENU_REQUEST, _GETMENU_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=688,
)

_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = services_dot_ServiceStatus__pb2._SERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_PING_OPERATION.fields_by_name['request'].message_type = _PING_REQUEST
_PING_OPERATION.fields_by_name['response'].message_type = _PING_RESPONSE
_PING_OPERATION.containing_type = _PING
_GETMENU_REQUEST.fields_by_name['section'].enum_type = products_dot_menu_dot_Section__pb2._SECTION
_GETMENU_REQUEST.containing_type = _GETMENU
_GETMENU_RESPONSE.fields_by_name['catalog'].message_type = products_dot_menu_dot_Menu__pb2._MENU
_GETMENU_RESPONSE.containing_type = _GETMENU
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['GetMenu'] = _GETMENU
DESCRIPTOR.enum_types_by_name['MenuError'] = _MENUERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.Ping.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PING_OPERATION,
    __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.Ping.Operation)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)
_sym_db.RegisterMessage(Ping.Operation)

GetMenu = _reflection.GeneratedProtocolMessageType('GetMenu', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _GETMENU_REQUEST,
    __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.GetMenu.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _GETMENU_RESPONSE,
    __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.GetMenu.Response)
    ))
  ,
  DESCRIPTOR = _GETMENU,
  __module__ = 'menu.v1beta1.MenuService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.menu.v1beta1.GetMenu)
  ))
_sym_db.RegisterMessage(GetMenu)
_sym_db.RegisterMessage(GetMenu.Request)
_sym_db.RegisterMessage(GetMenu.Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n(io.bloombox.schema.services.menu.v1beta1H\001P\001\242\002\003BBS'))

_MENU = _descriptor.ServiceDescriptor(
  name='Menu',
  full_name='bloombox.schema.services.menu.v1beta1.Menu',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=846,
  serialized_end=1261,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.menu.v1beta1.Menu.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\024\022\022/menu/v1beta1/ping')),
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='bloombox.schema.services.menu.v1beta1.Menu.Retrieve',
    index=1,
    containing_service=None,
    input_type=_GETMENU_REQUEST,
    output_type=_GETMENU_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\201\001\022</menu/v1beta1/{scope=partners/*/locations/*}/global:retrieveZA\022?/menu/v1beta1/{scope=partners/*/locations/*}/{section}:retrieve')),
  ),
])
_sym_db.RegisterServiceDescriptor(_MENU)

DESCRIPTOR.services_by_name['Menu'] = _MENU

# @@protoc_insertion_point(module_scope)
