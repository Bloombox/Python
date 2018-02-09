# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content/MaterialsData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from structs import Grow_pb2 as structs_dot_Grow__pb2
from structs import Shelf_pb2 as structs_dot_Shelf__pb2
from structs import Species_pb2 as structs_dot_Species__pb2
from structs import Genetics_pb2 as structs_dot_Genetics__pb2
from products.distribution import DistributionChannel_pb2 as products_dot_distribution_dot_DistributionChannel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='content/MaterialsData.proto',
  package='opencannabis.content',
  syntax='proto3',
  serialized_pb=_b('\n\x1b\x63ontent/MaterialsData.proto\x12\x14opencannabis.content\x1a\x12structs/Grow.proto\x1a\x13structs/Shelf.proto\x1a\x15structs/Species.proto\x1a\x16structs/Genetics.proto\x1a/products/distribution/DistributionChannel.proto\"\x91\x02\n\rMaterialsData\x12.\n\x07species\x18\x01 \x01(\x0e\x32\x1d.opencannabis.structs.Species\x12\x30\n\x08genetics\x18\x02 \x01(\x0b\x32\x1e.opencannabis.structs.Genetics\x12(\n\x04grow\x18\x03 \x01(\x0e\x32\x1a.opencannabis.structs.Grow\x12*\n\x05shelf\x18\x04 \x01(\x0e\x32\x1b.opencannabis.structs.Shelf\x12H\n\x08\x63hannels\x18\x05 \x03(\x0b\x32\x36.opencannabis.products.distribution.DistributionPolicyB<\n\x1eio.opencannabis.schema.contentB\x10MaterialsContentH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[structs_dot_Grow__pb2.DESCRIPTOR,structs_dot_Shelf__pb2.DESCRIPTOR,structs_dot_Species__pb2.DESCRIPTOR,structs_dot_Genetics__pb2.DESCRIPTOR,products_dot_distribution_dot_DistributionChannel__pb2.DESCRIPTOR,])




_MATERIALSDATA = _descriptor.Descriptor(
  name='MaterialsData',
  full_name='opencannabis.content.MaterialsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='species', full_name='opencannabis.content.MaterialsData.species', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genetics', full_name='opencannabis.content.MaterialsData.genetics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grow', full_name='opencannabis.content.MaterialsData.grow', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelf', full_name='opencannabis.content.MaterialsData.shelf', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='opencannabis.content.MaterialsData.channels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=191,
  serialized_end=464,
)

_MATERIALSDATA.fields_by_name['species'].enum_type = structs_dot_Species__pb2._SPECIES
_MATERIALSDATA.fields_by_name['genetics'].message_type = structs_dot_Genetics__pb2._GENETICS
_MATERIALSDATA.fields_by_name['grow'].enum_type = structs_dot_Grow__pb2._GROW
_MATERIALSDATA.fields_by_name['shelf'].enum_type = structs_dot_Shelf__pb2._SHELF
_MATERIALSDATA.fields_by_name['channels'].message_type = products_dot_distribution_dot_DistributionChannel__pb2._DISTRIBUTIONPOLICY
DESCRIPTOR.message_types_by_name['MaterialsData'] = _MATERIALSDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaterialsData = _reflection.GeneratedProtocolMessageType('MaterialsData', (_message.Message,), dict(
  DESCRIPTOR = _MATERIALSDATA,
  __module__ = 'content.MaterialsData_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.content.MaterialsData)
  ))
_sym_db.RegisterMessage(MaterialsData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.contentB\020MaterialsContentH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
