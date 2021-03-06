# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs/pricing/PricingDescriptor.proto

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


from commerce import Currency_pb2 as commerce_dot_Currency__pb2
from structs.pricing import SaleDescriptor_pb2 as structs_dot_pricing_dot_SaleDescriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='structs/pricing/PricingDescriptor.proto',
  package='opencannabis.structs.pricing',
  syntax='proto3',
  serialized_pb=_b('\n\'structs/pricing/PricingDescriptor.proto\x12\x1copencannabis.structs.pricing\x1a\x17\x63ommerce/Currency.proto\x1a$structs/pricing/SaleDescriptor.proto\"=\n\x17PricingTierAvailability\x12\x0f\n\x07offered\x18\x01 \x01(\x08\x12\x11\n\tavailable\x18\x02 \x01(\x08\"\xd4\x01\n\x15UnitPricingDescriptor\x12\x33\n\x05price\x18\x01 \x01(\x0b\x32$.opencannabis.commerce.CurrencyValue\x12\x45\n\x06status\x18\x02 \x01(\x0b\x32\x35.opencannabis.structs.pricing.PricingTierAvailability\x12?\n\tdiscounts\x18\x03 \x03(\x0b\x32,.opencannabis.structs.pricing.SaleDescriptor\"\xb8\x01\n\x19WeightedPricingDescriptor\x12?\n\x06weight\x18\x01 \x01(\x0e\x32/.opencannabis.structs.pricing.PricingWeightTier\x12\x41\n\x04tier\x18\x02 \x01(\x0b\x32\x33.opencannabis.structs.pricing.UnitPricingDescriptor\x12\x17\n\x0fweight_in_grams\x18\x03 \x01(\x02\"\xe6\x01\n\x11PricingDescriptor\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).opencannabis.structs.pricing.PricingType\x12\x43\n\x04unit\x18\x14 \x01(\x0b\x32\x33.opencannabis.structs.pricing.UnitPricingDescriptorH\x00\x12K\n\x08weighted\x18\x15 \x01(\x0b\x32\x37.opencannabis.structs.pricing.WeightedPricingDescriptorH\x00\x42\x06\n\x04tier\"\x94\x01\n\x0eProductPricing\x12?\n\tdiscounts\x18\x01 \x03(\x0b\x32,.opencannabis.structs.pricing.SaleDescriptor\x12\x41\n\x08manifest\x18\x02 \x03(\x0b\x32/.opencannabis.structs.pricing.PricingDescriptor*%\n\x0bPricingType\x12\x08\n\x04UNIT\x10\x00\x12\x0c\n\x08WEIGHTED\x10\x01*\xab\x01\n\x11PricingWeightTier\x12\r\n\tNO_WEIGHT\x10\x00\x12\x08\n\x04GRAM\x10\x01\x12\x0c\n\x08HALFGRAM\x10\x02\x12\x0f\n\x0bQUARTERGRAM\x10\x03\x12\x07\n\x03\x44UB\x10\x04\x12\n\n\x06\x45IGHTH\x10\x05\x12\x0b\n\x07QUARTER\x10\x06\x12\x08\n\x04HALF\x10\x07\x12\t\n\x05OUNCE\x10\x08\x12\t\n\x05POUND\x10\t\x12\x08\n\x04KILO\x10\n\x12\x07\n\x03TON\x10\x0b\x12\t\n\x05OTHER\x10\x0c\x42\x45\n%io.opencannabis.schema.product.structB\x12ProductPricingSpecH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[commerce_dot_Currency__pb2.DESCRIPTOR,structs_dot_pricing_dot_SaleDescriptor__pb2.DESCRIPTOR,])

_PRICINGTYPE = _descriptor.EnumDescriptor(
  name='PricingType',
  full_name='opencannabis.structs.pricing.PricingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHTED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=985,
  serialized_end=1022,
)
_sym_db.RegisterEnumDescriptor(_PRICINGTYPE)

PricingType = enum_type_wrapper.EnumTypeWrapper(_PRICINGTYPE)
_PRICINGWEIGHTTIER = _descriptor.EnumDescriptor(
  name='PricingWeightTier',
  full_name='opencannabis.structs.pricing.PricingWeightTier',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_WEIGHT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALFGRAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARTERGRAM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUB', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EIGHTH', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARTER', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALF', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUNCE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POUND', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILO', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TON', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1025,
  serialized_end=1196,
)
_sym_db.RegisterEnumDescriptor(_PRICINGWEIGHTTIER)

PricingWeightTier = enum_type_wrapper.EnumTypeWrapper(_PRICINGWEIGHTTIER)
UNIT = 0
WEIGHTED = 1
NO_WEIGHT = 0
GRAM = 1
HALFGRAM = 2
QUARTERGRAM = 3
DUB = 4
EIGHTH = 5
QUARTER = 6
HALF = 7
OUNCE = 8
POUND = 9
KILO = 10
TON = 11
OTHER = 12



_PRICINGTIERAVAILABILITY = _descriptor.Descriptor(
  name='PricingTierAvailability',
  full_name='opencannabis.structs.pricing.PricingTierAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offered', full_name='opencannabis.structs.pricing.PricingTierAvailability.offered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available', full_name='opencannabis.structs.pricing.PricingTierAvailability.available', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=197,
)


_UNITPRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='UnitPricingDescriptor',
  full_name='opencannabis.structs.pricing.UnitPricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='opencannabis.structs.pricing.UnitPricingDescriptor.price', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='opencannabis.structs.pricing.UnitPricingDescriptor.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discounts', full_name='opencannabis.structs.pricing.UnitPricingDescriptor.discounts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=200,
  serialized_end=412,
)


_WEIGHTEDPRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='WeightedPricingDescriptor',
  full_name='opencannabis.structs.pricing.WeightedPricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='opencannabis.structs.pricing.WeightedPricingDescriptor.weight', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tier', full_name='opencannabis.structs.pricing.WeightedPricingDescriptor.tier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_in_grams', full_name='opencannabis.structs.pricing.WeightedPricingDescriptor.weight_in_grams', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=415,
  serialized_end=599,
)


_PRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='PricingDescriptor',
  full_name='opencannabis.structs.pricing.PricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='opencannabis.structs.pricing.PricingDescriptor.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='opencannabis.structs.pricing.PricingDescriptor.unit', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted', full_name='opencannabis.structs.pricing.PricingDescriptor.weighted', index=2,
      number=21, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='tier', full_name='opencannabis.structs.pricing.PricingDescriptor.tier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=602,
  serialized_end=832,
)


_PRODUCTPRICING = _descriptor.Descriptor(
  name='ProductPricing',
  full_name='opencannabis.structs.pricing.ProductPricing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discounts', full_name='opencannabis.structs.pricing.ProductPricing.discounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='opencannabis.structs.pricing.ProductPricing.manifest', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=835,
  serialized_end=983,
)

_UNITPRICINGDESCRIPTOR.fields_by_name['price'].message_type = commerce_dot_Currency__pb2._CURRENCYVALUE
_UNITPRICINGDESCRIPTOR.fields_by_name['status'].message_type = _PRICINGTIERAVAILABILITY
_UNITPRICINGDESCRIPTOR.fields_by_name['discounts'].message_type = structs_dot_pricing_dot_SaleDescriptor__pb2._SALEDESCRIPTOR
_WEIGHTEDPRICINGDESCRIPTOR.fields_by_name['weight'].enum_type = _PRICINGWEIGHTTIER
_WEIGHTEDPRICINGDESCRIPTOR.fields_by_name['tier'].message_type = _UNITPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.fields_by_name['type'].enum_type = _PRICINGTYPE
_PRICINGDESCRIPTOR.fields_by_name['unit'].message_type = _UNITPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.fields_by_name['weighted'].message_type = _WEIGHTEDPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.oneofs_by_name['tier'].fields.append(
  _PRICINGDESCRIPTOR.fields_by_name['unit'])
_PRICINGDESCRIPTOR.fields_by_name['unit'].containing_oneof = _PRICINGDESCRIPTOR.oneofs_by_name['tier']
_PRICINGDESCRIPTOR.oneofs_by_name['tier'].fields.append(
  _PRICINGDESCRIPTOR.fields_by_name['weighted'])
_PRICINGDESCRIPTOR.fields_by_name['weighted'].containing_oneof = _PRICINGDESCRIPTOR.oneofs_by_name['tier']
_PRODUCTPRICING.fields_by_name['discounts'].message_type = structs_dot_pricing_dot_SaleDescriptor__pb2._SALEDESCRIPTOR
_PRODUCTPRICING.fields_by_name['manifest'].message_type = _PRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['PricingTierAvailability'] = _PRICINGTIERAVAILABILITY
DESCRIPTOR.message_types_by_name['UnitPricingDescriptor'] = _UNITPRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['WeightedPricingDescriptor'] = _WEIGHTEDPRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['PricingDescriptor'] = _PRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['ProductPricing'] = _PRODUCTPRICING
DESCRIPTOR.enum_types_by_name['PricingType'] = _PRICINGTYPE
DESCRIPTOR.enum_types_by_name['PricingWeightTier'] = _PRICINGWEIGHTTIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PricingTierAvailability = _reflection.GeneratedProtocolMessageType('PricingTierAvailability', (_message.Message,), dict(
  DESCRIPTOR = _PRICINGTIERAVAILABILITY,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.PricingTierAvailability)
  ))
_sym_db.RegisterMessage(PricingTierAvailability)

UnitPricingDescriptor = _reflection.GeneratedProtocolMessageType('UnitPricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _UNITPRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.UnitPricingDescriptor)
  ))
_sym_db.RegisterMessage(UnitPricingDescriptor)

WeightedPricingDescriptor = _reflection.GeneratedProtocolMessageType('WeightedPricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDPRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.WeightedPricingDescriptor)
  ))
_sym_db.RegisterMessage(WeightedPricingDescriptor)

PricingDescriptor = _reflection.GeneratedProtocolMessageType('PricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _PRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.PricingDescriptor)
  ))
_sym_db.RegisterMessage(PricingDescriptor)

ProductPricing = _reflection.GeneratedProtocolMessageType('ProductPricing', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTPRICING,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.ProductPricing)
  ))
_sym_db.RegisterMessage(ProductPricing)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.opencannabis.schema.product.structB\022ProductPricingSpecH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
