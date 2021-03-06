# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/settings/PartnerSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from contact import PhoneNumber_pb2 as contact_dot_PhoneNumber__pb2
from contact import EmailAddress_pb2 as contact_dot_EmailAddress__pb2
from partner.integrations import IntegrationSettings_pb2 as partner_dot_integrations_dot_IntegrationSettings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='partner/settings/PartnerSettings.proto',
  package='bloombox.schema.partner.settings',
  syntax='proto3',
  serialized_pb=_b('\n&partner/settings/PartnerSettings.proto\x12 bloombox.schema.partner.settings\x1a\x19\x63ontact/PhoneNumber.proto\x1a\x1a\x63ontact/EmailAddress.proto\x1a.partner/integrations/IntegrationSettings.proto\"\xa1\x01\n\x19PartnerNotificationTarget\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12\x32\n\x05phone\x18\n \x01(\x0b\x32!.opencannabis.contact.PhoneNumberH\x00\x12\x33\n\x05\x65mail\x18\x0b \x01(\x0b\x32\".opencannabis.contact.EmailAddressH\x00\x42\t\n\x07\x63ontact\"O\n\x1cPartnerEventAlertingSettings\x12\r\n\x05promo\x18\x01 \x01(\x08\x12\x10\n\x08security\x18\x02 \x01(\x08\x12\x0e\n\x06volume\x18\x03 \x01(\x08\"\xb7\x01\n\x14PartnerAlertSettings\x12N\n\x06\x65vents\x18\x01 \x01(\x0b\x32>.bloombox.schema.partner.settings.PartnerEventAlertingSettings\x12O\n\nrecipients\x18\x02 \x03(\x0b\x32;.bloombox.schema.partner.settings.PartnerNotificationTarget\"/\n\x0c\x42\x65taSettings\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x0f\n\x07sandbox\x18\x02 \x01(\x08\"`\n\rFeatureStatus\x12\x11\n\tanalytics\x18\x01 \x01(\x08\x12\x0c\n\x04\x62\x65ta\x18\x02 \x01(\x08\x12\x0f\n\x07offline\x18\x03 \x01(\x08\x12\x0c\n\x04shop\x18\x04 \x01(\x08\x12\x0f\n\x07\x63heckin\x18\x05 \x01(\x08\"0\n\x0eSearchSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05media\x18\x02 \x01(\x08\"\xf3\x02\n\x0fPartnerSettings\x12\x46\n\x06\x61lerts\x18\x01 \x01(\x0b\x32\x36.bloombox.schema.partner.settings.PartnerAlertSettings\x12<\n\x04\x62\x65ta\x18\x02 \x01(\x0b\x32..bloombox.schema.partner.settings.BetaSettings\x12\x41\n\x08\x66\x65\x61tures\x18\x03 \x01(\x0b\x32/.bloombox.schema.partner.settings.FeatureStatus\x12@\n\x06search\x18\x04 \x01(\x0b\x32\x30.bloombox.schema.partner.settings.SearchSettings\x12U\n\x0bintegration\x18\x07 \x01(\x0b\x32@.bloombox.schema.partner.integrations.PartnerIntegrationSettingsB/\n#io.bloombox.schema.partner.settingsH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[contact_dot_PhoneNumber__pb2.DESCRIPTOR,contact_dot_EmailAddress__pb2.DESCRIPTOR,partner_dot_integrations_dot_IntegrationSettings__pb2.DESCRIPTOR,])




_PARTNERNOTIFICATIONTARGET = _descriptor.Descriptor(
  name='PartnerNotificationTarget',
  full_name='bloombox.schema.partner.settings.PartnerNotificationTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='bloombox.schema.partner.settings.PartnerNotificationTarget.disabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone', full_name='bloombox.schema.partner.settings.PartnerNotificationTarget.phone', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='bloombox.schema.partner.settings.PartnerNotificationTarget.email', index=2,
      number=11, type=11, cpp_type=10, label=1,
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
      name='contact', full_name='bloombox.schema.partner.settings.PartnerNotificationTarget.contact',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=180,
  serialized_end=341,
)


_PARTNEREVENTALERTINGSETTINGS = _descriptor.Descriptor(
  name='PartnerEventAlertingSettings',
  full_name='bloombox.schema.partner.settings.PartnerEventAlertingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='promo', full_name='bloombox.schema.partner.settings.PartnerEventAlertingSettings.promo', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security', full_name='bloombox.schema.partner.settings.PartnerEventAlertingSettings.security', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='bloombox.schema.partner.settings.PartnerEventAlertingSettings.volume', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=343,
  serialized_end=422,
)


_PARTNERALERTSETTINGS = _descriptor.Descriptor(
  name='PartnerAlertSettings',
  full_name='bloombox.schema.partner.settings.PartnerAlertSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='bloombox.schema.partner.settings.PartnerAlertSettings.events', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipients', full_name='bloombox.schema.partner.settings.PartnerAlertSettings.recipients', index=1,
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
  serialized_start=425,
  serialized_end=608,
)


_BETASETTINGS = _descriptor.Descriptor(
  name='BetaSettings',
  full_name='bloombox.schema.partner.settings.BetaSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='bloombox.schema.partner.settings.BetaSettings.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sandbox', full_name='bloombox.schema.partner.settings.BetaSettings.sandbox', index=1,
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
  serialized_start=610,
  serialized_end=657,
)


_FEATURESTATUS = _descriptor.Descriptor(
  name='FeatureStatus',
  full_name='bloombox.schema.partner.settings.FeatureStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analytics', full_name='bloombox.schema.partner.settings.FeatureStatus.analytics', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta', full_name='bloombox.schema.partner.settings.FeatureStatus.beta', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offline', full_name='bloombox.schema.partner.settings.FeatureStatus.offline', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shop', full_name='bloombox.schema.partner.settings.FeatureStatus.shop', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkin', full_name='bloombox.schema.partner.settings.FeatureStatus.checkin', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=659,
  serialized_end=755,
)


_SEARCHSETTINGS = _descriptor.Descriptor(
  name='SearchSettings',
  full_name='bloombox.schema.partner.settings.SearchSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='bloombox.schema.partner.settings.SearchSettings.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='bloombox.schema.partner.settings.SearchSettings.media', index=1,
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
  serialized_start=757,
  serialized_end=805,
)


_PARTNERSETTINGS = _descriptor.Descriptor(
  name='PartnerSettings',
  full_name='bloombox.schema.partner.settings.PartnerSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alerts', full_name='bloombox.schema.partner.settings.PartnerSettings.alerts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta', full_name='bloombox.schema.partner.settings.PartnerSettings.beta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='bloombox.schema.partner.settings.PartnerSettings.features', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search', full_name='bloombox.schema.partner.settings.PartnerSettings.search', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integration', full_name='bloombox.schema.partner.settings.PartnerSettings.integration', index=4,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=808,
  serialized_end=1179,
)

_PARTNERNOTIFICATIONTARGET.fields_by_name['phone'].message_type = contact_dot_PhoneNumber__pb2._PHONENUMBER
_PARTNERNOTIFICATIONTARGET.fields_by_name['email'].message_type = contact_dot_EmailAddress__pb2._EMAILADDRESS
_PARTNERNOTIFICATIONTARGET.oneofs_by_name['contact'].fields.append(
  _PARTNERNOTIFICATIONTARGET.fields_by_name['phone'])
_PARTNERNOTIFICATIONTARGET.fields_by_name['phone'].containing_oneof = _PARTNERNOTIFICATIONTARGET.oneofs_by_name['contact']
_PARTNERNOTIFICATIONTARGET.oneofs_by_name['contact'].fields.append(
  _PARTNERNOTIFICATIONTARGET.fields_by_name['email'])
_PARTNERNOTIFICATIONTARGET.fields_by_name['email'].containing_oneof = _PARTNERNOTIFICATIONTARGET.oneofs_by_name['contact']
_PARTNERALERTSETTINGS.fields_by_name['events'].message_type = _PARTNEREVENTALERTINGSETTINGS
_PARTNERALERTSETTINGS.fields_by_name['recipients'].message_type = _PARTNERNOTIFICATIONTARGET
_PARTNERSETTINGS.fields_by_name['alerts'].message_type = _PARTNERALERTSETTINGS
_PARTNERSETTINGS.fields_by_name['beta'].message_type = _BETASETTINGS
_PARTNERSETTINGS.fields_by_name['features'].message_type = _FEATURESTATUS
_PARTNERSETTINGS.fields_by_name['search'].message_type = _SEARCHSETTINGS
_PARTNERSETTINGS.fields_by_name['integration'].message_type = partner_dot_integrations_dot_IntegrationSettings__pb2._PARTNERINTEGRATIONSETTINGS
DESCRIPTOR.message_types_by_name['PartnerNotificationTarget'] = _PARTNERNOTIFICATIONTARGET
DESCRIPTOR.message_types_by_name['PartnerEventAlertingSettings'] = _PARTNEREVENTALERTINGSETTINGS
DESCRIPTOR.message_types_by_name['PartnerAlertSettings'] = _PARTNERALERTSETTINGS
DESCRIPTOR.message_types_by_name['BetaSettings'] = _BETASETTINGS
DESCRIPTOR.message_types_by_name['FeatureStatus'] = _FEATURESTATUS
DESCRIPTOR.message_types_by_name['SearchSettings'] = _SEARCHSETTINGS
DESCRIPTOR.message_types_by_name['PartnerSettings'] = _PARTNERSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PartnerNotificationTarget = _reflection.GeneratedProtocolMessageType('PartnerNotificationTarget', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERNOTIFICATIONTARGET,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.PartnerNotificationTarget)
  ))
_sym_db.RegisterMessage(PartnerNotificationTarget)

PartnerEventAlertingSettings = _reflection.GeneratedProtocolMessageType('PartnerEventAlertingSettings', (_message.Message,), dict(
  DESCRIPTOR = _PARTNEREVENTALERTINGSETTINGS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.PartnerEventAlertingSettings)
  ))
_sym_db.RegisterMessage(PartnerEventAlertingSettings)

PartnerAlertSettings = _reflection.GeneratedProtocolMessageType('PartnerAlertSettings', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERALERTSETTINGS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.PartnerAlertSettings)
  ))
_sym_db.RegisterMessage(PartnerAlertSettings)

BetaSettings = _reflection.GeneratedProtocolMessageType('BetaSettings', (_message.Message,), dict(
  DESCRIPTOR = _BETASETTINGS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.BetaSettings)
  ))
_sym_db.RegisterMessage(BetaSettings)

FeatureStatus = _reflection.GeneratedProtocolMessageType('FeatureStatus', (_message.Message,), dict(
  DESCRIPTOR = _FEATURESTATUS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.FeatureStatus)
  ))
_sym_db.RegisterMessage(FeatureStatus)

SearchSettings = _reflection.GeneratedProtocolMessageType('SearchSettings', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHSETTINGS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.SearchSettings)
  ))
_sym_db.RegisterMessage(SearchSettings)

PartnerSettings = _reflection.GeneratedProtocolMessageType('PartnerSettings', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERSETTINGS,
  __module__ = 'partner.settings.PartnerSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.settings.PartnerSettings)
  ))
_sym_db.RegisterMessage(PartnerSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#io.bloombox.schema.partner.settingsH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
