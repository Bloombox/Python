# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/Datamodel.proto

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


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/Datamodel.proto',
  package='core',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x63ore/Datamodel.proto\x12\x04\x63ore\x1a google/protobuf/descriptor.proto\"F\n\x12PersistenceOptions\x12\"\n\x04mode\x18\x01 \x01(\x0e\x32\x14.core.CollectionMode\x12\x0c\n\x04path\x18\x02 \x01(\t\"1\n\x0cTableOptions\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"E\n\x11SubmessageOptions\x12\"\n\x04mode\x18\x01 \x01(\x0e\x32\x14.core.CollectionMode\x12\x0c\n\x04path\x18\x03 \x01(\t\"M\n\x17\x46ieldPersistenceOptions\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.core.FieldType\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"D\n\x11TableFieldOptions\x12\x0f\n\x07require\x18\x01 \x01(\x08\x12\x0e\n\x06ignore\x18\x02 \x01(\x08\x12\x0e\n\x06\x62qtype\x18\x03 \x01(\t*7\n\x0e\x43ollectionMode\x12\n\n\x06NESTED\x10\x00\x12\x0e\n\nCOLLECTION\x10\x01\x12\t\n\x05GROUP\x10\x02*4\n\tFieldType\x12\x0c\n\x08STANDARD\x10\x00\x12\x07\n\x03KEY\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x08\n\x04TAGS\x10\x03:F\n\x02\x64\x62\x12\x1f.google.protobuf.MessageOptions\x18\xf0. \x01(\x0b\x32\x18.core.PersistenceOptions:C\n\x05table\x12\x1f.google.protobuf.MessageOptions\x18\xf1. \x01(\x0b\x32\x12.core.TableOptions:L\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xd8\x36 \x01(\x0b\x32\x1d.core.FieldPersistenceOptions:G\n\x06\x63olumn\x12\x1d.google.protobuf.FieldOptions\x18\xd9\x36 \x01(\x0b\x32\x17.core.TableFieldOptions:K\n\ncollection\x12\x1d.google.protobuf.FieldOptions\x18\xda\x36 \x01(\x0b\x32\x17.core.SubmessageOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_COLLECTIONMODE = _descriptor.EnumDescriptor(
  name='CollectionMode',
  full_name='core.CollectionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NESTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=407,
  serialized_end=462,
)
_sym_db.RegisterEnumDescriptor(_COLLECTIONMODE)

CollectionMode = enum_type_wrapper.EnumTypeWrapper(_COLLECTIONMODE)
_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='core.FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAGS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=464,
  serialized_end=516,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
NESTED = 0
COLLECTION = 1
GROUP = 2
STANDARD = 0
KEY = 1
ID = 2
TAGS = 3

DB_FIELD_NUMBER = 6000
db = _descriptor.FieldDescriptor(
  name='db', full_name='core.db', index=0,
  number=6000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
TABLE_FIELD_NUMBER = 6001
table = _descriptor.FieldDescriptor(
  name='table', full_name='core.table', index=1,
  number=6001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
FIELD_FIELD_NUMBER = 7000
field = _descriptor.FieldDescriptor(
  name='field', full_name='core.field', index=2,
  number=7000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
COLUMN_FIELD_NUMBER = 7001
column = _descriptor.FieldDescriptor(
  name='column', full_name='core.column', index=3,
  number=7001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
COLLECTION_FIELD_NUMBER = 7002
collection = _descriptor.FieldDescriptor(
  name='collection', full_name='core.collection', index=4,
  number=7002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_PERSISTENCEOPTIONS = _descriptor.Descriptor(
  name='PersistenceOptions',
  full_name='core.PersistenceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='core.PersistenceOptions.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='core.PersistenceOptions.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=64,
  serialized_end=134,
)


_TABLEOPTIONS = _descriptor.Descriptor(
  name='TableOptions',
  full_name='core.TableOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.TableOptions.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='core.TableOptions.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=136,
  serialized_end=185,
)


_SUBMESSAGEOPTIONS = _descriptor.Descriptor(
  name='SubmessageOptions',
  full_name='core.SubmessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='core.SubmessageOptions.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='core.SubmessageOptions.path', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=187,
  serialized_end=256,
)


_FIELDPERSISTENCEOPTIONS = _descriptor.Descriptor(
  name='FieldPersistenceOptions',
  full_name='core.FieldPersistenceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.FieldPersistenceOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='core.FieldPersistenceOptions.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=258,
  serialized_end=335,
)


_TABLEFIELDOPTIONS = _descriptor.Descriptor(
  name='TableFieldOptions',
  full_name='core.TableFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='require', full_name='core.TableFieldOptions.require', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignore', full_name='core.TableFieldOptions.ignore', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bqtype', full_name='core.TableFieldOptions.bqtype', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=337,
  serialized_end=405,
)

_PERSISTENCEOPTIONS.fields_by_name['mode'].enum_type = _COLLECTIONMODE
_SUBMESSAGEOPTIONS.fields_by_name['mode'].enum_type = _COLLECTIONMODE
_FIELDPERSISTENCEOPTIONS.fields_by_name['type'].enum_type = _FIELDTYPE
DESCRIPTOR.message_types_by_name['PersistenceOptions'] = _PERSISTENCEOPTIONS
DESCRIPTOR.message_types_by_name['TableOptions'] = _TABLEOPTIONS
DESCRIPTOR.message_types_by_name['SubmessageOptions'] = _SUBMESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['FieldPersistenceOptions'] = _FIELDPERSISTENCEOPTIONS
DESCRIPTOR.message_types_by_name['TableFieldOptions'] = _TABLEFIELDOPTIONS
DESCRIPTOR.enum_types_by_name['CollectionMode'] = _COLLECTIONMODE
DESCRIPTOR.enum_types_by_name['FieldType'] = _FIELDTYPE
DESCRIPTOR.extensions_by_name['db'] = db
DESCRIPTOR.extensions_by_name['table'] = table
DESCRIPTOR.extensions_by_name['field'] = field
DESCRIPTOR.extensions_by_name['column'] = column
DESCRIPTOR.extensions_by_name['collection'] = collection
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersistenceOptions = _reflection.GeneratedProtocolMessageType('PersistenceOptions', (_message.Message,), dict(
  DESCRIPTOR = _PERSISTENCEOPTIONS,
  __module__ = 'core.Datamodel_pb2'
  # @@protoc_insertion_point(class_scope:core.PersistenceOptions)
  ))
_sym_db.RegisterMessage(PersistenceOptions)

TableOptions = _reflection.GeneratedProtocolMessageType('TableOptions', (_message.Message,), dict(
  DESCRIPTOR = _TABLEOPTIONS,
  __module__ = 'core.Datamodel_pb2'
  # @@protoc_insertion_point(class_scope:core.TableOptions)
  ))
_sym_db.RegisterMessage(TableOptions)

SubmessageOptions = _reflection.GeneratedProtocolMessageType('SubmessageOptions', (_message.Message,), dict(
  DESCRIPTOR = _SUBMESSAGEOPTIONS,
  __module__ = 'core.Datamodel_pb2'
  # @@protoc_insertion_point(class_scope:core.SubmessageOptions)
  ))
_sym_db.RegisterMessage(SubmessageOptions)

FieldPersistenceOptions = _reflection.GeneratedProtocolMessageType('FieldPersistenceOptions', (_message.Message,), dict(
  DESCRIPTOR = _FIELDPERSISTENCEOPTIONS,
  __module__ = 'core.Datamodel_pb2'
  # @@protoc_insertion_point(class_scope:core.FieldPersistenceOptions)
  ))
_sym_db.RegisterMessage(FieldPersistenceOptions)

TableFieldOptions = _reflection.GeneratedProtocolMessageType('TableFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _TABLEFIELDOPTIONS,
  __module__ = 'core.Datamodel_pb2'
  # @@protoc_insertion_point(class_scope:core.TableFieldOptions)
  ))
_sym_db.RegisterMessage(TableFieldOptions)

db.message_type = _PERSISTENCEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(db)
table.message_type = _TABLEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(table)
field.message_type = _FIELDPERSISTENCEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)
column.message_type = _TABLEFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(column)
collection.message_type = _SUBMESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(collection)

# @@protoc_insertion_point(module_scope)
