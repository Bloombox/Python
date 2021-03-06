# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact/EmailAddress.proto

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
  name='contact/EmailAddress.proto',
  package='opencannabis.contact',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x63ontact/EmailAddress.proto\x12\x14opencannabis.contact\x1a\x0e\x62q_field.proto\"\xe8\x01\n\x0c\x45mailAddress\x12M\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB<\x8a@9Email address, in standard format (\'example@sample.com\').\x12?\n\tvalidated\x18\x02 \x01(\x08\x42,\x8a@)Validation status for this email address.\x12H\n\x04name\x18\x03 \x01(\tB:\x8a@7Display name for the email address, if known/specified.B8\n\x1eio.opencannabis.schema.contactB\x0c\x43ontactEmailH\x01P\x00\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,])




_EMAILADDRESS = _descriptor.Descriptor(
  name='EmailAddress',
  full_name='opencannabis.contact.EmailAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='opencannabis.contact.EmailAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@9Email address, in standard format (\'example@sample.com\').')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validated', full_name='opencannabis.contact.EmailAddress.validated', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@)Validation status for this email address.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='opencannabis.contact.EmailAddress.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@7Display name for the email address, if known/specified.')), file=DESCRIPTOR),
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
  serialized_start=69,
  serialized_end=301,
)

DESCRIPTOR.message_types_by_name['EmailAddress'] = _EMAILADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmailAddress = _reflection.GeneratedProtocolMessageType('EmailAddress', (_message.Message,), dict(
  DESCRIPTOR = _EMAILADDRESS,
  __module__ = 'contact.EmailAddress_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.contact.EmailAddress)
  ))
_sym_db.RegisterMessage(EmailAddress)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.contactB\014ContactEmailH\001P\000\242\002\003OCS'))
_EMAILADDRESS.fields_by_name['address'].has_options = True
_EMAILADDRESS.fields_by_name['address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@9Email address, in standard format (\'example@sample.com\').'))
_EMAILADDRESS.fields_by_name['validated'].has_options = True
_EMAILADDRESS.fields_by_name['validated']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@)Validation status for this email address.'))
_EMAILADDRESS.fields_by_name['name'].has_options = True
_EMAILADDRESS.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@7Display name for the email address, if known/specified.'))
# @@protoc_insertion_point(module_scope)
