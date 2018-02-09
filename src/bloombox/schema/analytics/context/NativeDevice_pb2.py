# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/context/NativeDevice.proto

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
from device import Device_pb2 as device_dot_Device__pb2
from structs import Version_pb2 as structs_dot_Version__pb2
from analytics.context import OS_pb2 as analytics_dot_context_dot_OS__pb2
from analytics.context import Application_pb2 as analytics_dot_context_dot_Application__pb2
from proximity import BluetoothBeacon_pb2 as proximity_dot_BluetoothBeacon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/context/NativeDevice.proto',
  package='bloombox.schema.analytics.context',
  syntax='proto3',
  serialized_pb=_b('\n$analytics/context/NativeDevice.proto\x12!bloombox.schema.analytics.context\x1a\x0e\x62q_field.proto\x1a\x13\x64\x65vice/Device.proto\x1a\x15structs/Version.proto\x1a\x1a\x61nalytics/context/OS.proto\x1a#analytics/context/Application.proto\x1a\x1fproximity/BluetoothBeacon.proto\"\x93\x01\n\tPixelSize\x12\x41\n\x05width\x18\x01 \x01(\rB2\xf0?\x01\x8a@,Specifies the width portion of a pixel size.\x12\x43\n\x06height\x18\x02 \x01(\rB3\xf0?\x01\x8a@-Specifies the height portion of a pixel size.\"\x9c\x03\n\x0c\x44\x65viceScreen\x12T\n\x06screen\x18\x01 \x01(\x0b\x32,.bloombox.schema.analytics.context.PixelSizeB\x16\x8a@\x13Size of the screen.\x12X\n\x08viewport\x18\x02 \x01(\x0b\x32,.bloombox.schema.analytics.context.PixelSizeB\x18\x8a@\x15Size of the viewport.\x12\x41\n\x07\x64\x65nsity\x18\x03 \x01(\rB0\x8a@-Specifies the height portion of a pixel size.\x12\x98\x01\n\x0borientation\x18\x04 \x01(\x0e\x32\x34.bloombox.schema.analytics.context.ScreenOrientationBM\x8a@JSpecifies the orientation of the screen at the time an event was captured.\"\x81\x05\n\x13NativeDeviceContext\x12Y\n\x04type\x18\x01 \x01(\x0e\x32\x1f.opencannabis.device.DeviceTypeB*\xf0?\x01\x8a@$Specifies the type of native device.\x12k\n\x04role\x18\x02 \x01(\x0e\x32-.bloombox.schema.analytics.context.DeviceRoleB.\xf0?\x01\x8a@(Specifies the role of the native device.\x12\x65\n\x02os\x18\x03 \x01(\x0b\x32+.bloombox.schema.analytics.context.DeviceOSB,\xf0?\x01\x8a@&Specifies the OS of the native device.\x12h\n\x06\x62\x65\x61\x63on\x18\x06 \x01(\x0b\x32\'.opencannabis.proximity.BluetoothBeaconB/\x80@\x01\x8a@)BLE signal broadcasting from this device.\x12g\n\twitnessed\x18\x07 \x03(\x0b\x32\'.opencannabis.proximity.BluetoothBeaconB+\x80@\x01\x8a@%BLE signals witnessed by this device.\x12h\n\x06screen\x18\x04 \x01(\x0b\x32/.bloombox.schema.analytics.context.DeviceScreenB\'\x8a@$Information about the device screen.*$\n\nDeviceRole\x12\n\n\x06\x43LIENT\x10\x00\x12\n\n\x06SERVER\x10\x01*M\n\x11ScreenOrientation\x12\x1b\n\x17UNSPECIFIED_ORIENTATION\x10\x00\x12\x0c\n\x08PORTRAIT\x10\x01\x12\r\n\tLANDSCAPE\x10\x02\x42?\n$io.bloombox.schema.telemetry.contextB\rDeviceContextH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,device_dot_Device__pb2.DESCRIPTOR,structs_dot_Version__pb2.DESCRIPTOR,analytics_dot_context_dot_OS__pb2.DESCRIPTOR,analytics_dot_context_dot_Application__pb2.DESCRIPTOR,proximity_dot_BluetoothBeacon__pb2.DESCRIPTOR,])

_DEVICEROLE = _descriptor.EnumDescriptor(
  name='DeviceRole',
  full_name='bloombox.schema.analytics.context.DeviceRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLIENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1442,
  serialized_end=1478,
)
_sym_db.RegisterEnumDescriptor(_DEVICEROLE)

DeviceRole = enum_type_wrapper.EnumTypeWrapper(_DEVICEROLE)
_SCREENORIENTATION = _descriptor.EnumDescriptor(
  name='ScreenOrientation',
  full_name='bloombox.schema.analytics.context.ScreenOrientation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_ORIENTATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PORTRAIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANDSCAPE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1480,
  serialized_end=1557,
)
_sym_db.RegisterEnumDescriptor(_SCREENORIENTATION)

ScreenOrientation = enum_type_wrapper.EnumTypeWrapper(_SCREENORIENTATION)
CLIENT = 0
SERVER = 1
UNSPECIFIED_ORIENTATION = 0
PORTRAIT = 1
LANDSCAPE = 2



_PIXELSIZE = _descriptor.Descriptor(
  name='PixelSize',
  full_name='bloombox.schema.analytics.context.PixelSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='bloombox.schema.analytics.context.PixelSize.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@,Specifies the width portion of a pixel size.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='bloombox.schema.analytics.context.PixelSize.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@-Specifies the height portion of a pixel size.')), file=DESCRIPTOR),
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
  serialized_start=234,
  serialized_end=381,
)


_DEVICESCREEN = _descriptor.Descriptor(
  name='DeviceScreen',
  full_name='bloombox.schema.analytics.context.DeviceScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='screen', full_name='bloombox.schema.analytics.context.DeviceScreen.screen', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\023Size of the screen.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewport', full_name='bloombox.schema.analytics.context.DeviceScreen.viewport', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\025Size of the viewport.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='density', full_name='bloombox.schema.analytics.context.DeviceScreen.density', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-Specifies the height portion of a pixel size.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='bloombox.schema.analytics.context.DeviceScreen.orientation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@JSpecifies the orientation of the screen at the time an event was captured.')), file=DESCRIPTOR),
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
  serialized_start=384,
  serialized_end=796,
)


_NATIVEDEVICECONTEXT = _descriptor.Descriptor(
  name='NativeDeviceContext',
  full_name='bloombox.schema.analytics.context.NativeDeviceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bloombox.schema.analytics.context.NativeDeviceContext.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@$Specifies the type of native device.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='bloombox.schema.analytics.context.NativeDeviceContext.role', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@(Specifies the role of the native device.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os', full_name='bloombox.schema.analytics.context.NativeDeviceContext.os', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@&Specifies the OS of the native device.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beacon', full_name='bloombox.schema.analytics.context.NativeDeviceContext.beacon', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@)BLE signal broadcasting from this device.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witnessed', full_name='bloombox.schema.analytics.context.NativeDeviceContext.witnessed', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@%BLE signals witnessed by this device.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='screen', full_name='bloombox.schema.analytics.context.NativeDeviceContext.screen', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@$Information about the device screen.')), file=DESCRIPTOR),
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
  serialized_start=799,
  serialized_end=1440,
)

_DEVICESCREEN.fields_by_name['screen'].message_type = _PIXELSIZE
_DEVICESCREEN.fields_by_name['viewport'].message_type = _PIXELSIZE
_DEVICESCREEN.fields_by_name['orientation'].enum_type = _SCREENORIENTATION
_NATIVEDEVICECONTEXT.fields_by_name['type'].enum_type = device_dot_Device__pb2._DEVICETYPE
_NATIVEDEVICECONTEXT.fields_by_name['role'].enum_type = _DEVICEROLE
_NATIVEDEVICECONTEXT.fields_by_name['os'].message_type = analytics_dot_context_dot_OS__pb2._DEVICEOS
_NATIVEDEVICECONTEXT.fields_by_name['beacon'].message_type = proximity_dot_BluetoothBeacon__pb2._BLUETOOTHBEACON
_NATIVEDEVICECONTEXT.fields_by_name['witnessed'].message_type = proximity_dot_BluetoothBeacon__pb2._BLUETOOTHBEACON
_NATIVEDEVICECONTEXT.fields_by_name['screen'].message_type = _DEVICESCREEN
DESCRIPTOR.message_types_by_name['PixelSize'] = _PIXELSIZE
DESCRIPTOR.message_types_by_name['DeviceScreen'] = _DEVICESCREEN
DESCRIPTOR.message_types_by_name['NativeDeviceContext'] = _NATIVEDEVICECONTEXT
DESCRIPTOR.enum_types_by_name['DeviceRole'] = _DEVICEROLE
DESCRIPTOR.enum_types_by_name['ScreenOrientation'] = _SCREENORIENTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PixelSize = _reflection.GeneratedProtocolMessageType('PixelSize', (_message.Message,), dict(
  DESCRIPTOR = _PIXELSIZE,
  __module__ = 'analytics.context.NativeDevice_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.context.PixelSize)
  ))
_sym_db.RegisterMessage(PixelSize)

DeviceScreen = _reflection.GeneratedProtocolMessageType('DeviceScreen', (_message.Message,), dict(
  DESCRIPTOR = _DEVICESCREEN,
  __module__ = 'analytics.context.NativeDevice_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.context.DeviceScreen)
  ))
_sym_db.RegisterMessage(DeviceScreen)

NativeDeviceContext = _reflection.GeneratedProtocolMessageType('NativeDeviceContext', (_message.Message,), dict(
  DESCRIPTOR = _NATIVEDEVICECONTEXT,
  __module__ = 'analytics.context.NativeDevice_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.context.NativeDeviceContext)
  ))
_sym_db.RegisterMessage(NativeDeviceContext)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.bloombox.schema.telemetry.contextB\rDeviceContextH\001P\000\242\002\003BBS'))
_PIXELSIZE.fields_by_name['width'].has_options = True
_PIXELSIZE.fields_by_name['width']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@,Specifies the width portion of a pixel size.'))
_PIXELSIZE.fields_by_name['height'].has_options = True
_PIXELSIZE.fields_by_name['height']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@-Specifies the height portion of a pixel size.'))
_DEVICESCREEN.fields_by_name['screen'].has_options = True
_DEVICESCREEN.fields_by_name['screen']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\023Size of the screen.'))
_DEVICESCREEN.fields_by_name['viewport'].has_options = True
_DEVICESCREEN.fields_by_name['viewport']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\025Size of the viewport.'))
_DEVICESCREEN.fields_by_name['density'].has_options = True
_DEVICESCREEN.fields_by_name['density']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-Specifies the height portion of a pixel size.'))
_DEVICESCREEN.fields_by_name['orientation'].has_options = True
_DEVICESCREEN.fields_by_name['orientation']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@JSpecifies the orientation of the screen at the time an event was captured.'))
_NATIVEDEVICECONTEXT.fields_by_name['type'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@$Specifies the type of native device.'))
_NATIVEDEVICECONTEXT.fields_by_name['role'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@(Specifies the role of the native device.'))
_NATIVEDEVICECONTEXT.fields_by_name['os'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['os']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@&Specifies the OS of the native device.'))
_NATIVEDEVICECONTEXT.fields_by_name['beacon'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['beacon']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@)BLE signal broadcasting from this device.'))
_NATIVEDEVICECONTEXT.fields_by_name['witnessed'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['witnessed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@%BLE signals witnessed by this device.'))
_NATIVEDEVICECONTEXT.fields_by_name['screen'].has_options = True
_NATIVEDEVICECONTEXT.fields_by_name['screen']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@$Information about the device screen.'))
# @@protoc_insertion_point(module_scope)
