# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/Preroll.proto

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
from content import MaterialsData_pb2 as content_dot_MaterialsData__pb2
from content import ProductContent_pb2 as content_dot_ProductContent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='products/Preroll.proto',
  package='opencannabis.products',
  syntax='proto3',
  serialized_pb=_b('\n\x16products/Preroll.proto\x12\x15opencannabis.products\x1a\x15\x62\x61se/ProductKey.proto\x1a\x1b\x63ontent/MaterialsData.proto\x1a\x1c\x63ontent/ProductContent.proto\"\xae\x02\n\x07Preroll\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12\x33\n\x06\x66lower\x18\x02 \x01(\x0b\x32#.opencannabis.base.ProductReference\x12\x0e\n\x06length\x18\x03 \x01(\x01\x12\x11\n\tthickness\x18\x04 \x01(\x01\x12\x31\n\x05\x66lags\x18\x05 \x03(\x0e\x32\".opencannabis.products.PrerollFlag\x12\x35\n\x07product\x18\x06 \x01(\x0b\x32$.opencannabis.content.ProductContent\x12\x35\n\x08material\x18\x07 \x01(\x0b\x32#.opencannabis.content.MaterialsData*}\n\x0bPrerollFlag\x12\x14\n\x10NO_PREROLL_FLAGS\x10\x00\x12\x10\n\x0cHASH_INFUSED\x10\x01\x12\x10\n\x0cKIEF_INFUSED\x10\x02\x12\r\n\tFORTIFIED\x10\x03\x12\x0f\n\x0b\x46ULL_FLOWER\x10\x04\x12\x14\n\x10\x43ONTAINS_TOBACCO\x10\x05\x42\x37\n\x1eio.opencannabis.schema.productB\x0ePrerollProductH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[base_dot_ProductKey__pb2.DESCRIPTOR,content_dot_MaterialsData__pb2.DESCRIPTOR,content_dot_ProductContent__pb2.DESCRIPTOR,])

_PREROLLFLAG = _descriptor.EnumDescriptor(
  name='PrerollFlag',
  full_name='opencannabis.products.PrerollFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_PREROLL_FLAGS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HASH_INFUSED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIEF_INFUSED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORTIFIED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_FLOWER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINS_TOBACCO', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=436,
  serialized_end=561,
)
_sym_db.RegisterEnumDescriptor(_PREROLLFLAG)

PrerollFlag = enum_type_wrapper.EnumTypeWrapper(_PREROLLFLAG)
NO_PREROLL_FLAGS = 0
HASH_INFUSED = 1
KIEF_INFUSED = 2
FORTIFIED = 3
FULL_FLOWER = 4
CONTAINS_TOBACCO = 5



_PREROLL = _descriptor.Descriptor(
  name='Preroll',
  full_name='opencannabis.products.Preroll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opencannabis.products.Preroll.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flower', full_name='opencannabis.products.Preroll.flower', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='opencannabis.products.Preroll.length', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thickness', full_name='opencannabis.products.Preroll.thickness', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='opencannabis.products.Preroll.flags', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='opencannabis.products.Preroll.product', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material', full_name='opencannabis.products.Preroll.material', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=132,
  serialized_end=434,
)

_PREROLL.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_PREROLL.fields_by_name['flower'].message_type = base_dot_ProductKey__pb2._PRODUCTREFERENCE
_PREROLL.fields_by_name['flags'].enum_type = _PREROLLFLAG
_PREROLL.fields_by_name['product'].message_type = content_dot_ProductContent__pb2._PRODUCTCONTENT
_PREROLL.fields_by_name['material'].message_type = content_dot_MaterialsData__pb2._MATERIALSDATA
DESCRIPTOR.message_types_by_name['Preroll'] = _PREROLL
DESCRIPTOR.enum_types_by_name['PrerollFlag'] = _PREROLLFLAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Preroll = _reflection.GeneratedProtocolMessageType('Preroll', (_message.Message,), dict(
  DESCRIPTOR = _PREROLL,
  __module__ = 'products.Preroll_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.Preroll)
  ))
_sym_db.RegisterMessage(Preroll)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.productB\016PrerollProductH\001P\000\370\001\001'))
# @@protoc_insertion_point(module_scope)
