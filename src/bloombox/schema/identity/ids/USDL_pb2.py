# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/ids/USDL.proto

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


import bq_field_pb2 as bq__field__pb2
from geo import USState_pb2 as geo_dot_USState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/ids/USDL.proto',
  package='bloombox.schema.identity.ids',
  syntax='proto3',
  serialized_pb=_b('\n\x17identity/ids/USDL.proto\x12\x1c\x62loombox.schema.identity.ids\x1a\x0e\x62q_field.proto\x1a\x11geo/USState.proto\"\xc3\x01\n\x0eUSDLFieldValue\x12^\n\x05\x66ield\x18\x01 \x01(\x0e\x32\'.bloombox.schema.identity.ids.USDLFieldB&\x8a@#Field that we are storing data for.\x12/\n\x05value\x18\x02 \x01(\tB\x1e\x8a@\x1bString data for this field.H\x00\x12\x18\n\traw_value\x18\x03 \x01(\x0c\x42\x03\x80@\x01H\x00\x42\x06\n\x04\x64\x61ta\"\xe6\x02\n\x04USDL\x12\x14\n\x07\x62\x61rcode\x18\x01 \x01(\tB\x03\x80@\x01\x12\x16\n\tmagstripe\x18\x02 \x01(\tB\x03\x80@\x01\x12`\n\x0cjurisdiction\x18\x03 \x01(\x0e\x32\x1d.opencannabis.geo.usa.USStateB+\x8a@(State that issued this Driver\'s License.\x12k\n\x13identification_card\x18\x04 \x01(\x08\x42N\x8a@KFlag that indicates this is an identification card, not a Driver\'s License.\x12\x61\n\x06\x66ields\x18\x64 \x03(\x0b\x32,.bloombox.schema.identity.ids.USDLFieldValueB#\x8a@ Raw field data for this license.*\xb8\x05\n\tUSDLField\x12\x10\n\x0c\x42\x41\x43K_BARCODE\x10\x00\x12\x0f\n\x0b\x46\x41MILY_NAME\x10\x01\x12\x0e\n\nGIVEN_NAME\x10\x02\x12\x0f\n\x0bMIDDLE_NAME\x10\x03\x12\r\n\tFULL_NAME\x10\x04\x12\x0f\n\x0bNAME_PREFIX\x10\x05\x12\x0f\n\x0bNAME_SUFFIX\x10\x06\x12\x11\n\rDATE_OF_BIRTH\x10\n\x12\x07\n\x03SEX\x10\x0b\x12\n\n\x06HEIGHT\x10\x0c\x12\n\n\x06WEIGHT\x10\r\x12\r\n\tEYE_COLOR\x10\x0e\x12\x0e\n\nHAIR_COLOR\x10\x0f\x12\x10\n\x0c\x46ULL_ADDRESS\x10\x14\x12\x10\n\x0c\x41\x44\x44RESS_LINE\x10\x15\x12\x11\n\rADDRESS_LINE2\x10\x16\x12\x10\n\x0c\x41\x44\x44RESS_CITY\x10\x17\x12\x0f\n\x0bPOSTAL_CODE\x10\x18\x12\x16\n\x12STATE_JURISDICTION\x10\x19\x12\x0e\n\nLICENSE_ID\x10\x1e\x12\x16\n\x12LICENSE_ISSUE_DATE\x10\x1f\x12\x17\n\x13LICENSE_EXPIRY_DATE\x10 \x12\x17\n\x13ISSUER_JURISDICTION\x10!\x12&\n\"ISSUER_JURISDICTION_FORMAT_VERSION\x10\"\x12\x18\n\x14UNIQUE_DOCUMENT_CODE\x10(\x12\x1a\n\x16INVENTORY_CONTROL_CODE\x10)\x12\x11\n\rUNDER_18_DATE\x10\x32\x12\x11\n\rUNDER_19_DATE\x10\x33\x12\x11\n\rUNDER_21_DATE\x10\x34\x12\x0c\n\x08UNDER_18\x10<\x12\x0c\n\x08UNDER_19\x10=\x12\x0c\n\x08UNDER_21\x10>\x12\x0f\n\x0bORGAN_DONOR\x10?\x12\x0b\n\x07VETERAN\x10@\x12\x0f\n\x0bNONRESIDENT\x10\x41\x12\x12\n\x0eRACE_ETHNICITY\x10\x46\x12\x13\n\x0f\x43OMPLIANCE_TYPE\x10GB+\n\x1fio.bloombox.schema.identity.idsH\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,geo_dot_USState__pb2.DESCRIPTOR,])

_USDLFIELD = _descriptor.EnumDescriptor(
  name='USDLField',
  full_name='bloombox.schema.identity.ids.USDLField',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BACK_BARCODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_NAME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIVEN_NAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_NAME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_NAME', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_PREFIX', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_SUFFIX', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_OF_BIRTH', index=7, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEX', index=8, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEIGHT', index=9, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHT', index=10, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EYE_COLOR', index=11, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAIR_COLOR', index=12, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_ADDRESS', index=13, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_LINE', index=14, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_LINE2', index=15, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_CITY', index=16, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL_CODE', index=17, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_JURISDICTION', index=18, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENSE_ID', index=19, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENSE_ISSUE_DATE', index=20, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENSE_EXPIRY_DATE', index=21, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISSUER_JURISDICTION', index=22, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISSUER_JURISDICTION_FORMAT_VERSION', index=23, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIQUE_DOCUMENT_CODE', index=24, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVENTORY_CONTROL_CODE', index=25, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_18_DATE', index=26, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_19_DATE', index=27, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_21_DATE', index=28, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_18', index=29, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_19', index=30, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_21', index=31, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGAN_DONOR', index=32, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VETERAN', index=33, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONRESIDENT', index=34, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RACE_ETHNICITY', index=35, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLIANCE_TYPE', index=36, number=71,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=652,
  serialized_end=1348,
)
_sym_db.RegisterEnumDescriptor(_USDLFIELD)

USDLField = enum_type_wrapper.EnumTypeWrapper(_USDLFIELD)
BACK_BARCODE = 0
FAMILY_NAME = 1
GIVEN_NAME = 2
MIDDLE_NAME = 3
FULL_NAME = 4
NAME_PREFIX = 5
NAME_SUFFIX = 6
DATE_OF_BIRTH = 10
SEX = 11
HEIGHT = 12
WEIGHT = 13
EYE_COLOR = 14
HAIR_COLOR = 15
FULL_ADDRESS = 20
ADDRESS_LINE = 21
ADDRESS_LINE2 = 22
ADDRESS_CITY = 23
POSTAL_CODE = 24
STATE_JURISDICTION = 25
LICENSE_ID = 30
LICENSE_ISSUE_DATE = 31
LICENSE_EXPIRY_DATE = 32
ISSUER_JURISDICTION = 33
ISSUER_JURISDICTION_FORMAT_VERSION = 34
UNIQUE_DOCUMENT_CODE = 40
INVENTORY_CONTROL_CODE = 41
UNDER_18_DATE = 50
UNDER_19_DATE = 51
UNDER_21_DATE = 52
UNDER_18 = 60
UNDER_19 = 61
UNDER_21 = 62
ORGAN_DONOR = 63
VETERAN = 64
NONRESIDENT = 65
RACE_ETHNICITY = 70
COMPLIANCE_TYPE = 71



_USDLFIELDVALUE = _descriptor.Descriptor(
  name='USDLFieldValue',
  full_name='bloombox.schema.identity.ids.USDLFieldValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='bloombox.schema.identity.ids.USDLFieldValue.field', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@#Field that we are storing data for.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bloombox.schema.identity.ids.USDLFieldValue.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\033String data for this field.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='bloombox.schema.identity.ids.USDLFieldValue.raw_value', index=2,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='bloombox.schema.identity.ids.USDLFieldValue.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=93,
  serialized_end=288,
)


_USDL = _descriptor.Descriptor(
  name='USDL',
  full_name='bloombox.schema.identity.ids.USDL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='barcode', full_name='bloombox.schema.identity.ids.USDL.barcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magstripe', full_name='bloombox.schema.identity.ids.USDL.magstripe', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jurisdiction', full_name='bloombox.schema.identity.ids.USDL.jurisdiction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@(State that issued this Driver\'s License.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identification_card', full_name='bloombox.schema.identity.ids.USDL.identification_card', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@KFlag that indicates this is an identification card, not a Driver\'s License.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='bloombox.schema.identity.ids.USDL.fields', index=4,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Raw field data for this license.')), file=DESCRIPTOR),
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
  serialized_start=291,
  serialized_end=649,
)

_USDLFIELDVALUE.fields_by_name['field'].enum_type = _USDLFIELD
_USDLFIELDVALUE.oneofs_by_name['data'].fields.append(
  _USDLFIELDVALUE.fields_by_name['value'])
_USDLFIELDVALUE.fields_by_name['value'].containing_oneof = _USDLFIELDVALUE.oneofs_by_name['data']
_USDLFIELDVALUE.oneofs_by_name['data'].fields.append(
  _USDLFIELDVALUE.fields_by_name['raw_value'])
_USDLFIELDVALUE.fields_by_name['raw_value'].containing_oneof = _USDLFIELDVALUE.oneofs_by_name['data']
_USDL.fields_by_name['jurisdiction'].enum_type = geo_dot_USState__pb2._USSTATE
_USDL.fields_by_name['fields'].message_type = _USDLFIELDVALUE
DESCRIPTOR.message_types_by_name['USDLFieldValue'] = _USDLFIELDVALUE
DESCRIPTOR.message_types_by_name['USDL'] = _USDL
DESCRIPTOR.enum_types_by_name['USDLField'] = _USDLFIELD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

USDLFieldValue = _reflection.GeneratedProtocolMessageType('USDLFieldValue', (_message.Message,), dict(
  DESCRIPTOR = _USDLFIELDVALUE,
  __module__ = 'identity.ids.USDL_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.identity.ids.USDLFieldValue)
  ))
_sym_db.RegisterMessage(USDLFieldValue)

USDL = _reflection.GeneratedProtocolMessageType('USDL', (_message.Message,), dict(
  DESCRIPTOR = _USDL,
  __module__ = 'identity.ids.USDL_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.identity.ids.USDL)
  ))
_sym_db.RegisterMessage(USDL)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037io.bloombox.schema.identity.idsH\001P\001\242\002\003BBS'))
_USDLFIELDVALUE.fields_by_name['field'].has_options = True
_USDLFIELDVALUE.fields_by_name['field']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@#Field that we are storing data for.'))
_USDLFIELDVALUE.fields_by_name['value'].has_options = True
_USDLFIELDVALUE.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\033String data for this field.'))
_USDLFIELDVALUE.fields_by_name['raw_value'].has_options = True
_USDLFIELDVALUE.fields_by_name['raw_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001'))
_USDL.fields_by_name['barcode'].has_options = True
_USDL.fields_by_name['barcode']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001'))
_USDL.fields_by_name['magstripe'].has_options = True
_USDL.fields_by_name['magstripe']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001'))
_USDL.fields_by_name['jurisdiction'].has_options = True
_USDL.fields_by_name['jurisdiction']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@(State that issued this Driver\'s License.'))
_USDL.fields_by_name['identification_card'].has_options = True
_USDL.fields_by_name['identification_card']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@KFlag that indicates this is an identification card, not a Driver\'s License.'))
_USDL.fields_by_name['fields'].has_options = True
_USDL.fields_by_name['fields']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Raw field data for this license.'))
# @@protoc_insertion_point(module_scope)
