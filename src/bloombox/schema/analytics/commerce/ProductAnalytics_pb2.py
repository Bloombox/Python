# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/commerce/ProductAnalytics.proto

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


from base import ProductKey_pb2 as base_dot_ProductKey__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/commerce/ProductAnalytics.proto',
  package='bloombox.schema.analytics.product',
  syntax='proto3',
  serialized_pb=_b('\n)analytics/commerce/ProductAnalytics.proto\x12!bloombox.schema.analytics.product\x1a\x15\x62\x61se/ProductKey.proto\x1a\x16temporal/Instant.proto\"\x8c\x01\n\nImpression\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12\x10\n\x08\x66iltered\x18\x02 \x01(\x08\x12\x0e\n\x06sorted\x18\x03 \x01(\x08\x12\x30\n\x08occurred\x18\x04 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\"y\n\x04View\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12\x13\n\x0binteractive\x18\x02 \x01(\x08\x12\x30\n\x08occurred\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\"\xa6\x01\n\x06\x41\x63tion\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.opencannabis.base.ProductKey\x12>\n\x04verb\x18\x02 \x01(\x0e\x32\x30.bloombox.schema.analytics.product.ProductAction\x12\x30\n\x08occurred\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant*\x8a\x01\n\rProductAction\x12\x08\n\x04VIEW\x10\x00\x12\t\n\x05SHARE\x10\x01\x12\x0c\n\x08\x46\x41VORITE\x10\x02\x12\x0b\n\x07\x43OMPARE\x10\x03\x12\x08\n\x04\x43\x41RT\x10\x04\x12\x0c\n\x08PURCHASE\x10\x05\x12\r\n\tSUBSCRIBE\x10\x06\x12\x08\n\x04ZOOM\x10\x07\x12\x0b\n\x07REPORTS\x10\x08\x12\x0b\n\x07SIMILAR\x10\tBB\n$io.bloombox.schema.analytics.productB\x10ProductAnalyticsH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[base_dot_ProductKey__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,])

_PRODUCTACTION = _descriptor.EnumDescriptor(
  name='ProductAction',
  full_name='bloombox.schema.analytics.product.ProductAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAVORITE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPARE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CART', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZOOM', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPORTS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=563,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTACTION)

ProductAction = enum_type_wrapper.EnumTypeWrapper(_PRODUCTACTION)
VIEW = 0
SHARE = 1
FAVORITE = 2
COMPARE = 3
CART = 4
PURCHASE = 5
SUBSCRIBE = 6
ZOOM = 7
REPORTS = 8
SIMILAR = 9



_IMPRESSION = _descriptor.Descriptor(
  name='Impression',
  full_name='bloombox.schema.analytics.product.Impression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.analytics.product.Impression.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filtered', full_name='bloombox.schema.analytics.product.Impression.filtered', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sorted', full_name='bloombox.schema.analytics.product.Impression.sorted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.product.Impression.occurred', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=128,
  serialized_end=268,
)


_VIEW = _descriptor.Descriptor(
  name='View',
  full_name='bloombox.schema.analytics.product.View',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.analytics.product.View.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive', full_name='bloombox.schema.analytics.product.View.interactive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.product.View.occurred', index=2,
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
  serialized_start=270,
  serialized_end=391,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='bloombox.schema.analytics.product.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.analytics.product.Action.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verb', full_name='bloombox.schema.analytics.product.Action.verb', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.product.Action.occurred', index=2,
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
  serialized_start=394,
  serialized_end=560,
)

_IMPRESSION.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_IMPRESSION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
_VIEW.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_VIEW.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
_ACTION.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_ACTION.fields_by_name['verb'].enum_type = _PRODUCTACTION
_ACTION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['Impression'] = _IMPRESSION
DESCRIPTOR.message_types_by_name['View'] = _VIEW
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['ProductAction'] = _PRODUCTACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Impression = _reflection.GeneratedProtocolMessageType('Impression', (_message.Message,), dict(
  DESCRIPTOR = _IMPRESSION,
  __module__ = 'analytics.commerce.ProductAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.product.Impression)
  ))
_sym_db.RegisterMessage(Impression)

View = _reflection.GeneratedProtocolMessageType('View', (_message.Message,), dict(
  DESCRIPTOR = _VIEW,
  __module__ = 'analytics.commerce.ProductAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.product.View)
  ))
_sym_db.RegisterMessage(View)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'analytics.commerce.ProductAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.product.Action)
  ))
_sym_db.RegisterMessage(Action)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.bloombox.schema.analytics.productB\020ProductAnalyticsH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
