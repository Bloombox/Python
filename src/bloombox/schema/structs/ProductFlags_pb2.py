# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs/ProductFlags.proto

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
  name='structs/ProductFlags.proto',
  package='opencannabis.structs',
  syntax='proto3',
  serialized_pb=_b('\n\x1astructs/ProductFlags.proto\x12\x14opencannabis.structs*\xa6\x01\n\x0bProductFlag\x12\x0b\n\x07VISIBLE\x10\x00\x12\n\n\x06HIDDEN\x10\x01\x12\x0b\n\x07PREMIUM\x10\x02\x12\x0c\n\x08\x46\x45\x41TURED\x10\x03\x12\x0b\n\x07ORGANIC\x10\x04\x12\r\n\tEXCLUSIVE\x10\x05\x12\x0c\n\x08IN_HOUSE\x10\x06\x12\x0f\n\x0bLAST_CHANCE\x10\x07\x12\x10\n\x0cLIMITED_TIME\x10\x08\x12\x0b\n\x07ON_SALE\x10\t\x12\t\n\x05LOCAL\x10\nB;\n%io.opencannabis.schema.product.structB\x0b\x42\x61seStructsH\x01P\x01\xf8\x01\x01\x62\x06proto3')
)

_PRODUCTFLAG = _descriptor.EnumDescriptor(
  name='ProductFlag',
  full_name='opencannabis.structs.ProductFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VISIBLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIDDEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGANIC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_HOUSE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_CHANCE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIMITED_TIME', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_SALE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=53,
  serialized_end=219,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTFLAG)

ProductFlag = enum_type_wrapper.EnumTypeWrapper(_PRODUCTFLAG)
VISIBLE = 0
HIDDEN = 1
PREMIUM = 2
FEATURED = 3
ORGANIC = 4
EXCLUSIVE = 5
IN_HOUSE = 6
LAST_CHANCE = 7
LIMITED_TIME = 8
ON_SALE = 9
LOCAL = 10


DESCRIPTOR.enum_types_by_name['ProductFlag'] = _PRODUCTFLAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.opencannabis.schema.product.structB\013BaseStructsH\001P\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
