# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/integrations/SendgridSettings.proto

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
  name='partner/integrations/SendgridSettings.proto',
  package='bloombox.schema.partner.integrations.sendgrid',
  syntax='proto3',
  serialized_pb=_b('\n+partner/integrations/SendgridSettings.proto\x12-bloombox.schema.partner.integrations.sendgrid\"\x1d\n\x1bSendgridIntegrationFeatures\"p\n\x10SendgridSettings\x12\\\n\x08\x66\x65\x61tures\x18\n \x01(\x0b\x32J.bloombox.schema.partner.integrations.sendgrid.SendgridIntegrationFeaturesB<\n0io.bloombox.schema.partner.integrations.sendgridH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
)




_SENDGRIDINTEGRATIONFEATURES = _descriptor.Descriptor(
  name='SendgridIntegrationFeatures',
  full_name='bloombox.schema.partner.integrations.sendgrid.SendgridIntegrationFeatures',
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
  serialized_start=94,
  serialized_end=123,
)


_SENDGRIDSETTINGS = _descriptor.Descriptor(
  name='SendgridSettings',
  full_name='bloombox.schema.partner.integrations.sendgrid.SendgridSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='bloombox.schema.partner.integrations.sendgrid.SendgridSettings.features', index=0,
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
  serialized_start=125,
  serialized_end=237,
)

_SENDGRIDSETTINGS.fields_by_name['features'].message_type = _SENDGRIDINTEGRATIONFEATURES
DESCRIPTOR.message_types_by_name['SendgridIntegrationFeatures'] = _SENDGRIDINTEGRATIONFEATURES
DESCRIPTOR.message_types_by_name['SendgridSettings'] = _SENDGRIDSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendgridIntegrationFeatures = _reflection.GeneratedProtocolMessageType('SendgridIntegrationFeatures', (_message.Message,), dict(
  DESCRIPTOR = _SENDGRIDINTEGRATIONFEATURES,
  __module__ = 'partner.integrations.SendgridSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.sendgrid.SendgridIntegrationFeatures)
  ))
_sym_db.RegisterMessage(SendgridIntegrationFeatures)

SendgridSettings = _reflection.GeneratedProtocolMessageType('SendgridSettings', (_message.Message,), dict(
  DESCRIPTOR = _SENDGRIDSETTINGS,
  __module__ = 'partner.integrations.SendgridSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.sendgrid.SendgridSettings)
  ))
_sym_db.RegisterMessage(SendgridSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n0io.bloombox.schema.partner.integrations.sendgridH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
