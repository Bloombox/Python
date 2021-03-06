# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/Merchandise.proto

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


from base import ProductKey_pb2 as base_dot_ProductKey__pb2
from content import ProductContent_pb2 as content_dot_ProductContent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='products/Merchandise.proto',
  package='opencannabis.products',
  syntax='proto3',
  serialized_pb=_b('\n\x1aproducts/Merchandise.proto\x12\x15opencannabis.products\x1a\x15\x62\x61se/ProductKey.proto\x1a\x1c\x63ontent/ProductContent.proto\"\xdd\x01\n\x0bMerchandise\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.opencannabis.products.MerchandiseType\x12\x35\n\x05\x66lags\x18\x03 \x03(\x0e\x32&.opencannabis.products.MerchandiseFlag\x12\x35\n\x07product\x18\x04 \x01(\x0b\x32$.opencannabis.content.ProductContent*g\n\x0fMerchandiseType\x12\x1b\n\x17UNSPECIFIED_MERCHANDISE\x10\x00\x12\x0c\n\x08\x43LOTHING\x10\x01\x12\r\n\tGLASSWARE\x10\x02\x12\r\n\tCONTAINER\x10\x03\x12\x0b\n\x07LIGHTER\x10\x04*M\n\x0fMerchandiseFlag\x12\x18\n\x14NO_MERCHANDISE_FLAGS\x10\x00\x12\x10\n\x0cMEDICAL_ONLY\x10\x01\x12\x0e\n\nBRAND_SWAG\x10\x02\x42>\n\x1eio.opencannabis.schema.productB\x12MerchandiseProductH\x01P\x00\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[base_dot_ProductKey__pb2.DESCRIPTOR,content_dot_ProductContent__pb2.DESCRIPTOR,])

_MERCHANDISETYPE = _descriptor.EnumDescriptor(
  name='MerchandiseType',
  full_name='opencannabis.products.MerchandiseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_MERCHANDISE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOTHING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLASSWARE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHTER', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=330,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_MERCHANDISETYPE)

MerchandiseType = enum_type_wrapper.EnumTypeWrapper(_MERCHANDISETYPE)
_MERCHANDISEFLAG = _descriptor.EnumDescriptor(
  name='MerchandiseFlag',
  full_name='opencannabis.products.MerchandiseFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_MERCHANDISE_FLAGS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDICAL_ONLY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRAND_SWAG', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=435,
  serialized_end=512,
)
_sym_db.RegisterEnumDescriptor(_MERCHANDISEFLAG)

MerchandiseFlag = enum_type_wrapper.EnumTypeWrapper(_MERCHANDISEFLAG)
UNSPECIFIED_MERCHANDISE = 0
CLOTHING = 1
GLASSWARE = 2
CONTAINER = 3
LIGHTER = 4
NO_MERCHANDISE_FLAGS = 0
MEDICAL_ONLY = 1
BRAND_SWAG = 2



_MERCHANDISE = _descriptor.Descriptor(
  name='Merchandise',
  full_name='opencannabis.products.Merchandise',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opencannabis.products.Merchandise.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='opencannabis.products.Merchandise.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='opencannabis.products.Merchandise.flags', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='opencannabis.products.Merchandise.product', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=107,
  serialized_end=328,
)

_MERCHANDISE.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_MERCHANDISE.fields_by_name['type'].enum_type = _MERCHANDISETYPE
_MERCHANDISE.fields_by_name['flags'].enum_type = _MERCHANDISEFLAG
_MERCHANDISE.fields_by_name['product'].message_type = content_dot_ProductContent__pb2._PRODUCTCONTENT
DESCRIPTOR.message_types_by_name['Merchandise'] = _MERCHANDISE
DESCRIPTOR.enum_types_by_name['MerchandiseType'] = _MERCHANDISETYPE
DESCRIPTOR.enum_types_by_name['MerchandiseFlag'] = _MERCHANDISEFLAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Merchandise = _reflection.GeneratedProtocolMessageType('Merchandise', (_message.Message,), dict(
  DESCRIPTOR = _MERCHANDISE,
  __module__ = 'products.Merchandise_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.Merchandise)
  ))
_sym_db.RegisterMessage(Merchandise)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.productB\022MerchandiseProductH\001P\000\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
