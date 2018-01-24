# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/context/Library.proto

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
from structs import Version_pb2 as structs_dot_Version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/context/Library.proto',
  package='bloombox.schema.analytics.context',
  syntax='proto3',
  serialized_pb=_b('\n\x1f\x61nalytics/context/Library.proto\x12!bloombox.schema.analytics.context\x1a\x0e\x62q_field.proto\x1a\x15structs/Version.proto\"\xe4\x02\n\rDeviceLibrary\x12O\n\x07variant\x18\x01 \x01(\tB>\xf0?\x01\x8a@8Variant name of the library being used to transmit data.\x12|\n\x07version\x18\x02 \x01(\x0b\x32!.opencannabis.structs.VersionSpecBH\xf0?\x01\x8a@BVersion specification for the library being used to transmit data.\x12\x83\x01\n\x06\x63lient\x18\x03 \x01(\x0e\x32,.bloombox.schema.analytics.context.APIClientBE\x8a@BSpecifies which internal Bloombox library sent this event, if any.*C\n\tAPIClient\x12\x10\n\x0cUNIDENTIFIED\x10\x00\x12\x0f\n\x0bJAVA_SCRIPT\x10\x01\x12\t\n\x05SWIFT\x10\x02\x12\x08\n\x04JAVA\x10\x03\x42=\n$io.bloombox.schema.telemetry.contextB\x0eLibraryContextH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,structs_dot_Version__pb2.DESCRIPTOR,])

_APICLIENT = _descriptor.EnumDescriptor(
  name='APIClient',
  full_name='bloombox.schema.analytics.context.APIClient',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNIDENTIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVA_SCRIPT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIFT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=468,
  serialized_end=535,
)
_sym_db.RegisterEnumDescriptor(_APICLIENT)

APIClient = enum_type_wrapper.EnumTypeWrapper(_APICLIENT)
UNIDENTIFIED = 0
JAVA_SCRIPT = 1
SWIFT = 2
JAVA = 3



_DEVICELIBRARY = _descriptor.Descriptor(
  name='DeviceLibrary',
  full_name='bloombox.schema.analytics.context.DeviceLibrary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant', full_name='bloombox.schema.analytics.context.DeviceLibrary.variant', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@8Variant name of the library being used to transmit data.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='bloombox.schema.analytics.context.DeviceLibrary.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@BVersion specification for the library being used to transmit data.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client', full_name='bloombox.schema.analytics.context.DeviceLibrary.client', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@BSpecifies which internal Bloombox library sent this event, if any.')), file=DESCRIPTOR),
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
  serialized_start=110,
  serialized_end=466,
)

_DEVICELIBRARY.fields_by_name['version'].message_type = structs_dot_Version__pb2._VERSIONSPEC
_DEVICELIBRARY.fields_by_name['client'].enum_type = _APICLIENT
DESCRIPTOR.message_types_by_name['DeviceLibrary'] = _DEVICELIBRARY
DESCRIPTOR.enum_types_by_name['APIClient'] = _APICLIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceLibrary = _reflection.GeneratedProtocolMessageType('DeviceLibrary', (_message.Message,), dict(
  DESCRIPTOR = _DEVICELIBRARY,
  __module__ = 'analytics.context.Library_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.context.DeviceLibrary)
  ))
_sym_db.RegisterMessage(DeviceLibrary)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.bloombox.schema.telemetry.contextB\016LibraryContextH\001P\000\370\001\001'))
_DEVICELIBRARY.fields_by_name['variant'].has_options = True
_DEVICELIBRARY.fields_by_name['variant']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@8Variant name of the library being used to transmit data.'))
_DEVICELIBRARY.fields_by_name['version'].has_options = True
_DEVICELIBRARY.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@BVersion specification for the library being used to transmit data.'))
_DEVICELIBRARY.fields_by_name['client'].has_options = True
_DEVICELIBRARY.fields_by_name['client']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@BSpecifies which internal Bloombox library sent this event, if any.'))
# @@protoc_insertion_point(module_scope)
