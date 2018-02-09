# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs/Species.proto

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
  name='structs/Species.proto',
  package='opencannabis.structs',
  syntax='proto3',
  serialized_pb=_b('\n\x15structs/Species.proto\x12\x14opencannabis.structs*d\n\x07Species\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06SATIVA\x10\x01\x12\x11\n\rHYBRID_SATIVA\x10\x02\x12\n\n\x06HYBRID\x10\x03\x12\x11\n\rHYBRID_INDICA\x10\x04\x12\n\n\x06INDICA\x10\x05\x42\x42\n%io.opencannabis.schema.product.structB\x0fMaterialSpeciesH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
)

_SPECIES = _descriptor.EnumDescriptor(
  name='Species',
  full_name='opencannabis.structs.Species',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SATIVA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYBRID_SATIVA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYBRID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYBRID_INDICA', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDICA', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=47,
  serialized_end=147,
)
_sym_db.RegisterEnumDescriptor(_SPECIES)

Species = enum_type_wrapper.EnumTypeWrapper(_SPECIES)
UNSPECIFIED = 0
SATIVA = 1
HYBRID_SATIVA = 2
HYBRID = 3
HYBRID_INDICA = 4
INDICA = 5


DESCRIPTOR.enum_types_by_name['Species'] = _SPECIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.opencannabis.schema.product.structB\017MaterialSpeciesH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
