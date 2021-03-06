# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/commerce/SectionAnalytics.proto

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


from temporal import Instant_pb2 as temporal_dot_Instant__pb2
from products.menu import Section_pb2 as products_dot_menu_dot_Section__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/commerce/SectionAnalytics.proto',
  package='bloombox.schema.analytics.section',
  syntax='proto3',
  serialized_pb=_b('\n)analytics/commerce/SectionAnalytics.proto\x12!bloombox.schema.analytics.section\x1a\x16temporal/Instant.proto\x1a\x1bproducts/menu/Section.proto\"}\n\nImpression\x12=\n\x04spec\x18\x01 \x01(\x0b\x32/.opencannabis.products.menu.section.SectionSpec\x12\x30\n\x08occurred\x18\x02 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\"\x8c\x01\n\x04View\x12=\n\x04spec\x18\x01 \x01(\x0b\x32/.opencannabis.products.menu.section.SectionSpec\x12\x13\n\x0binteractive\x18\x02 \x01(\x08\x12\x30\n\x08occurred\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\"\xb9\x01\n\x06\x41\x63tion\x12=\n\x04spec\x18\x01 \x01(\x0b\x32/.opencannabis.products.menu.section.SectionSpec\x12>\n\x04verb\x18\x02 \x01(\x0e\x32\x30.bloombox.schema.analytics.section.SectionAction\x12\x30\n\x08occurred\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant*/\n\rSectionAction\x12\x08\n\x04VIEW\x10\x00\x12\x08\n\x04SORT\x10\x01\x12\n\n\x06\x46ILTER\x10\x02\x42\x42\n$io.bloombox.schema.analytics.sectionB\x10SectionAnalyticsH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[temporal_dot_Instant__pb2.DESCRIPTOR,products_dot_menu_dot_Section__pb2.DESCRIPTOR,])

_SECTIONACTION = _descriptor.EnumDescriptor(
  name='SectionAction',
  full_name='bloombox.schema.analytics.section.SectionAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SORT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=591,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_SECTIONACTION)

SectionAction = enum_type_wrapper.EnumTypeWrapper(_SECTIONACTION)
VIEW = 0
SORT = 1
FILTER = 2



_IMPRESSION = _descriptor.Descriptor(
  name='Impression',
  full_name='bloombox.schema.analytics.section.Impression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='bloombox.schema.analytics.section.Impression.spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.section.Impression.occurred', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=133,
  serialized_end=258,
)


_VIEW = _descriptor.Descriptor(
  name='View',
  full_name='bloombox.schema.analytics.section.View',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='bloombox.schema.analytics.section.View.spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive', full_name='bloombox.schema.analytics.section.View.interactive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.section.View.occurred', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=261,
  serialized_end=401,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='bloombox.schema.analytics.section.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='bloombox.schema.analytics.section.Action.spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verb', full_name='bloombox.schema.analytics.section.Action.verb', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.section.Action.occurred', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=404,
  serialized_end=589,
)

_IMPRESSION.fields_by_name['spec'].message_type = products_dot_menu_dot_Section__pb2._SECTIONSPEC
_IMPRESSION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
_VIEW.fields_by_name['spec'].message_type = products_dot_menu_dot_Section__pb2._SECTIONSPEC
_VIEW.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
_ACTION.fields_by_name['spec'].message_type = products_dot_menu_dot_Section__pb2._SECTIONSPEC
_ACTION.fields_by_name['verb'].enum_type = _SECTIONACTION
_ACTION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['Impression'] = _IMPRESSION
DESCRIPTOR.message_types_by_name['View'] = _VIEW
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['SectionAction'] = _SECTIONACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Impression = _reflection.GeneratedProtocolMessageType('Impression', (_message.Message,), dict(
  DESCRIPTOR = _IMPRESSION,
  __module__ = 'analytics.commerce.SectionAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.section.Impression)
  ))
_sym_db.RegisterMessage(Impression)

View = _reflection.GeneratedProtocolMessageType('View', (_message.Message,), dict(
  DESCRIPTOR = _VIEW,
  __module__ = 'analytics.commerce.SectionAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.section.View)
  ))
_sym_db.RegisterMessage(View)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'analytics.commerce.SectionAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.section.Action)
  ))
_sym_db.RegisterMessage(Action)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.bloombox.schema.analytics.sectionB\020SectionAnalyticsH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
