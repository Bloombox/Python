# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person/Person.proto

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
from temporal import Date_pb2 as temporal_dot_Date__pb2
from contact import ContactInfo_pb2 as contact_dot_ContactInfo__pb2
from person import PersonName_pb2 as person_dot_PersonName__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='person/Person.proto',
  package='opencannabis.person',
  syntax='proto3',
  serialized_pb=_b('\n\x13person/Person.proto\x12\x13opencannabis.person\x1a\x0e\x62q_field.proto\x1a\x13temporal/Date.proto\x1a\x19\x63ontact/ContactInfo.proto\x1a\x17person/PersonName.proto\"\xbd\x03\n\x06Person\x12N\n\x04name\x18\x01 \x01(\x0b\x32\x19.opencannabis.person.NameB%\x8a@\"Person\'s primary name information.\x12m\n\nlegal_name\x18\x02 \x01(\x0b\x32\x19.opencannabis.person.NameB>\x8a@;Person\'s legal name, if it differs from their primary name.\x12W\n\x0e\x61lternate_name\x18\x03 \x01(\x0b\x32\x19.opencannabis.person.NameB$\x8a@!Person\'s optional alternate name.\x12T\n\x07\x63ontact\x18\x04 \x01(\x0b\x32!.opencannabis.contact.ContactInfoB \x8a@\x1dPerson\'s contact information.\x12\x45\n\rdate_of_birth\x18\x05 \x01(\x0b\x32\x1b.opencannabis.temporal.DateB\x11\x8a@\x0e\x44\x61te of birth.B)\n\x1dio.opencannabis.schema.personH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,temporal_dot_Date__pb2.DESCRIPTOR,contact_dot_ContactInfo__pb2.DESCRIPTOR,person_dot_PersonName__pb2.DESCRIPTOR,])




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='opencannabis.person.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='opencannabis.person.Person.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\"Person\'s primary name information.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legal_name', full_name='opencannabis.person.Person.legal_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Person\'s legal name, if it differs from their primary name.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alternate_name', full_name='opencannabis.person.Person.alternate_name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@!Person\'s optional alternate name.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contact', full_name='opencannabis.person.Person.contact', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\035Person\'s contact information.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='opencannabis.person.Person.date_of_birth', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\016Date of birth.')), file=DESCRIPTOR),
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
  serialized_start=134,
  serialized_end=579,
)

_PERSON.fields_by_name['name'].message_type = person_dot_PersonName__pb2._NAME
_PERSON.fields_by_name['legal_name'].message_type = person_dot_PersonName__pb2._NAME
_PERSON.fields_by_name['alternate_name'].message_type = person_dot_PersonName__pb2._NAME
_PERSON.fields_by_name['contact'].message_type = contact_dot_ContactInfo__pb2._CONTACTINFO
_PERSON.fields_by_name['date_of_birth'].message_type = temporal_dot_Date__pb2._DATE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'person.Person_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.person.Person)
  ))
_sym_db.RegisterMessage(Person)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035io.opencannabis.schema.personH\001P\001\242\002\003OCS'))
_PERSON.fields_by_name['name'].has_options = True
_PERSON.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\"Person\'s primary name information.'))
_PERSON.fields_by_name['legal_name'].has_options = True
_PERSON.fields_by_name['legal_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Person\'s legal name, if it differs from their primary name.'))
_PERSON.fields_by_name['alternate_name'].has_options = True
_PERSON.fields_by_name['alternate_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@!Person\'s optional alternate name.'))
_PERSON.fields_by_name['contact'].has_options = True
_PERSON.fields_by_name['contact']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\035Person\'s contact information.'))
_PERSON.fields_by_name['date_of_birth'].has_options = True
_PERSON.fields_by_name['date_of_birth']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\016Date of birth.'))
# @@protoc_insertion_point(module_scope)
