# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/integrations/GSuiteSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='partner/integrations/GSuiteSettings.proto',
  package='bloombox.schema.partner.integrations.gsuite',
  syntax='proto3',
  serialized_pb=_b('\n)partner/integrations/GSuiteSettings.proto\x12+bloombox.schema.partner.integrations.gsuite\"\x1b\n\x19GSuiteIntegrationFeatures\"z\n\x0eGSuiteSettings\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12X\n\x08\x66\x65\x61tures\x18\n \x01(\x0b\x32\x46.bloombox.schema.partner.integrations.gsuite.GSuiteIntegrationFeaturesB:\n.io.bloombox.schema.partner.integrations.gsuiteH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
)




_GSUITEINTEGRATIONFEATURES = _descriptor.Descriptor(
  name='GSuiteIntegrationFeatures',
  full_name='bloombox.schema.partner.integrations.gsuite.GSuiteIntegrationFeatures',
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
  serialized_start=90,
  serialized_end=117,
)


_GSUITESETTINGS = _descriptor.Descriptor(
  name='GSuiteSettings',
  full_name='bloombox.schema.partner.integrations.gsuite.GSuiteSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='bloombox.schema.partner.integrations.gsuite.GSuiteSettings.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='bloombox.schema.partner.integrations.gsuite.GSuiteSettings.features', index=1,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=241,
)

_GSUITESETTINGS.fields_by_name['features'].message_type = _GSUITEINTEGRATIONFEATURES
DESCRIPTOR.message_types_by_name['GSuiteIntegrationFeatures'] = _GSUITEINTEGRATIONFEATURES
DESCRIPTOR.message_types_by_name['GSuiteSettings'] = _GSUITESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GSuiteIntegrationFeatures = _reflection.GeneratedProtocolMessageType('GSuiteIntegrationFeatures', (_message.Message,), dict(
  DESCRIPTOR = _GSUITEINTEGRATIONFEATURES,
  __module__ = 'partner.integrations.GSuiteSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.gsuite.GSuiteIntegrationFeatures)
  ))
_sym_db.RegisterMessage(GSuiteIntegrationFeatures)

GSuiteSettings = _reflection.GeneratedProtocolMessageType('GSuiteSettings', (_message.Message,), dict(
  DESCRIPTOR = _GSUITESETTINGS,
  __module__ = 'partner.integrations.GSuiteSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.gsuite.GSuiteSettings)
  ))
_sym_db.RegisterMessage(GSuiteSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n.io.bloombox.schema.partner.integrations.gsuiteH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
