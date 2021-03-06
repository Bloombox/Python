# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/Flower.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  name='products/Flower.proto',
  package='opencannabis.products',
  syntax='proto3',
  serialized_pb=_b('\n\x15products/Flower.proto\x12\x15opencannabis.products\x1a\x15\x62\x61se/ProductKey.proto\x1a\x1b\x63ontent/MaterialsData.proto\x1a\x1c\x63ontent/ProductContent.proto\"\xa2\x01\n\x06\x46lower\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12\x35\n\x07product\x18\x02 \x01(\x0b\x32$.opencannabis.content.ProductContent\x12\x35\n\x08material\x18\x03 \x01(\x0b\x32#.opencannabis.content.MaterialsDataB9\n\x1eio.opencannabis.schema.productB\rFlowerProductH\x01P\x00\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[base_dot_ProductKey__pb2.DESCRIPTOR,content_dot_MaterialsData__pb2.DESCRIPTOR,content_dot_ProductContent__pb2.DESCRIPTOR,])




_FLOWER = _descriptor.Descriptor(
  name='Flower',
  full_name='opencannabis.products.Flower',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opencannabis.products.Flower.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='opencannabis.products.Flower.product', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material', full_name='opencannabis.products.Flower.material', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=131,
  serialized_end=293,
)

_FLOWER.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_FLOWER.fields_by_name['product'].message_type = content_dot_ProductContent__pb2._PRODUCTCONTENT
_FLOWER.fields_by_name['material'].message_type = content_dot_MaterialsData__pb2._MATERIALSDATA
DESCRIPTOR.message_types_by_name['Flower'] = _FLOWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Flower = _reflection.GeneratedProtocolMessageType('Flower', (_message.Message,), dict(
  DESCRIPTOR = _FLOWER,
  __module__ = 'products.Flower_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.Flower)
  ))
_sym_db.RegisterMessage(Flower)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.productB\rFlowerProductH\001P\000\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
