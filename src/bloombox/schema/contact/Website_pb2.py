# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact/Website.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bq_field_pb2 as bq__field__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contact/Website.proto',
  package='opencannabis.contact',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x63ontact/Website.proto\x12\x14opencannabis.contact\x1a\x0e\x62q_field.proto\"v\n\x07Website\x12$\n\x03uri\x18\x01 \x01(\tB\x17\x8a@\x14URI for the website.\x12\x32\n\x05title\x18\x02 \x01(\tB#\x8a@ Title from the HTML page at URI.\x12\x11\n\x04icon\x18\x03 \x01(\x0c\x42\x03\x80@\x01\x42:\n\x1eio.opencannabis.schema.contactB\x0e\x43ontactWebsiteH\x01P\x00\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,])




_WEBSITE = _descriptor.Descriptor(
  name='Website',
  full_name='opencannabis.contact.Website',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='opencannabis.contact.Website.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\024URI for the website.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='opencannabis.contact.Website.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Title from the HTML page at URI.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='opencannabis.contact.Website.icon', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001')), file=DESCRIPTOR),
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
  serialized_start=63,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['Website'] = _WEBSITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Website = _reflection.GeneratedProtocolMessageType('Website', (_message.Message,), dict(
  DESCRIPTOR = _WEBSITE,
  __module__ = 'contact.Website_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.contact.Website)
  ))
_sym_db.RegisterMessage(Website)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.contactB\016ContactWebsiteH\001P\000\242\002\003OCS'))
_WEBSITE.fields_by_name['uri'].has_options = True
_WEBSITE.fields_by_name['uri']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\024URI for the website.'))
_WEBSITE.fields_by_name['title'].has_options = True
_WEBSITE.fields_by_name['title']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Title from the HTML page at URI.'))
_WEBSITE.fields_by_name['icon'].has_options = True
_WEBSITE.fields_by_name['icon']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001'))
# @@protoc_insertion_point(module_scope)
