# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: media/MediaType.proto

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
  name='media/MediaType.proto',
  package='opencannabis.media',
  syntax='proto3',
  serialized_pb=_b('\n\x15media/MediaType.proto\x12\x12opencannabis.media\x1a\x0e\x62q_field.proto\"\x8a\x04\n\tMediaType\x12u\n\x04kind\x18\x01 \x01(\x0e\x32\".opencannabis.media.MediaType.KindBC\x8a@@Specifies the generic kind of media being described or attached.\x12h\n\nimage_type\x18\x65 \x01(\x0b\x32\x1d.opencannabis.media.ImageTypeB3\x8a@0Specifies content for an image-based media item.H\x00\x12q\n\rdocument_type\x18\xc9\x01 \x01(\x0b\x32 .opencannabis.media.DocumentTypeB5\x8a@2Specifies content for a document-based media item.H\x00\x12h\n\nvideo_type\x18\xad\x02 \x01(\x0b\x32\x1d.opencannabis.media.VideoTypeB2\x8a@/Specifies content for a video-based media item.H\x00\"4\n\x04Kind\x12\x08\n\x04LINK\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x0c\n\x08\x44OCUMENT\x10\x02\x12\t\n\x05VIDEO\x10\x03\x42\t\n\x07\x63ontent\"\xba\x01\n\tImageType\x12r\n\x04kind\x18\x01 \x01(\x0e\x32\'.opencannabis.media.ImageType.ImageKindB;\x8a@8Specifies the format of the attached or described image.\"9\n\tImageKind\x12\x07\n\x03PNG\x10\x00\x12\x07\n\x03JPG\x10\x01\x12\x07\n\x03GIF\x10\x02\x12\x07\n\x03SVG\x10\x03\x12\x08\n\x04WEBP\x10\x04\"\x9b\x02\n\x0c\x44ocumentType\x12{\n\x04kind\x18\x01 \x01(\x0e\x32-.opencannabis.media.DocumentType.DocumentKindB>\x8a@;Specifies the kind of document being attached or described.\x12T\n\ncompressed\x18\x02 \x01(\x08\x42@\x8a@=Specifies whether the attached document is compressed or not.\"8\n\x0c\x44ocumentKind\x12\x07\n\x03TXT\x10\x00\x12\x08\n\x04HTML\x10\x01\x12\x07\n\x03PDF\x10\x02\x12\x0c\n\x08MARKDOWN\x10\x03\"\xa7\x01\n\tVideoType\x12r\n\x04kind\x18\x01 \x01(\x0e\x32\'.opencannabis.media.VideoType.VideoKindB;\x8a@8Specifies the kind of video being attached or described.\"&\n\tVideoKind\x12\x07\n\x03MP4\x10\x00\x12\x07\n\x03\x46LV\x10\x01\x12\x07\n\x03HLS\x10\x02\x42\x37\n\x1cio.opencannabis.schema.mediaB\rMediaItemTypeH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,])



_MEDIATYPE_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='opencannabis.media.MediaType.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LINK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOCUMENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=521,
  serialized_end=573,
)
_sym_db.RegisterEnumDescriptor(_MEDIATYPE_KIND)

_IMAGETYPE_IMAGEKIND = _descriptor.EnumDescriptor(
  name='ImageKind',
  full_name='opencannabis.media.ImageType.ImageKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PNG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JPG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIF', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SVG', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEBP', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=716,
  serialized_end=773,
)
_sym_db.RegisterEnumDescriptor(_IMAGETYPE_IMAGEKIND)

_DOCUMENTTYPE_DOCUMENTKIND = _descriptor.EnumDescriptor(
  name='DocumentKind',
  full_name='opencannabis.media.DocumentType.DocumentKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TXT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PDF', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKDOWN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1003,
  serialized_end=1059,
)
_sym_db.RegisterEnumDescriptor(_DOCUMENTTYPE_DOCUMENTKIND)

_VIDEOTYPE_VIDEOKIND = _descriptor.EnumDescriptor(
  name='VideoKind',
  full_name='opencannabis.media.VideoType.VideoKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MP4', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLV', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HLS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1191,
  serialized_end=1229,
)
_sym_db.RegisterEnumDescriptor(_VIDEOTYPE_VIDEOKIND)


_MEDIATYPE = _descriptor.Descriptor(
  name='MediaType',
  full_name='opencannabis.media.MediaType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='opencannabis.media.MediaType.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@@Specifies the generic kind of media being described or attached.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='opencannabis.media.MediaType.image_type', index=1,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@0Specifies content for an image-based media item.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document_type', full_name='opencannabis.media.MediaType.document_type', index=2,
      number=201, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@2Specifies content for a document-based media item.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_type', full_name='opencannabis.media.MediaType.video_type', index=3,
      number=301, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@/Specifies content for a video-based media item.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIATYPE_KIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='opencannabis.media.MediaType.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=62,
  serialized_end=584,
)


_IMAGETYPE = _descriptor.Descriptor(
  name='ImageType',
  full_name='opencannabis.media.ImageType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='opencannabis.media.ImageType.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the format of the attached or described image.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGETYPE_IMAGEKIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=773,
)


_DOCUMENTTYPE = _descriptor.Descriptor(
  name='DocumentType',
  full_name='opencannabis.media.DocumentType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='opencannabis.media.DocumentType.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Specifies the kind of document being attached or described.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='opencannabis.media.DocumentType.compressed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@=Specifies whether the attached document is compressed or not.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOCUMENTTYPE_DOCUMENTKIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=776,
  serialized_end=1059,
)


_VIDEOTYPE = _descriptor.Descriptor(
  name='VideoType',
  full_name='opencannabis.media.VideoType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='opencannabis.media.VideoType.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the kind of video being attached or described.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIDEOTYPE_VIDEOKIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1229,
)

_MEDIATYPE.fields_by_name['kind'].enum_type = _MEDIATYPE_KIND
_MEDIATYPE.fields_by_name['image_type'].message_type = _IMAGETYPE
_MEDIATYPE.fields_by_name['document_type'].message_type = _DOCUMENTTYPE
_MEDIATYPE.fields_by_name['video_type'].message_type = _VIDEOTYPE
_MEDIATYPE_KIND.containing_type = _MEDIATYPE
_MEDIATYPE.oneofs_by_name['content'].fields.append(
  _MEDIATYPE.fields_by_name['image_type'])
_MEDIATYPE.fields_by_name['image_type'].containing_oneof = _MEDIATYPE.oneofs_by_name['content']
_MEDIATYPE.oneofs_by_name['content'].fields.append(
  _MEDIATYPE.fields_by_name['document_type'])
_MEDIATYPE.fields_by_name['document_type'].containing_oneof = _MEDIATYPE.oneofs_by_name['content']
_MEDIATYPE.oneofs_by_name['content'].fields.append(
  _MEDIATYPE.fields_by_name['video_type'])
_MEDIATYPE.fields_by_name['video_type'].containing_oneof = _MEDIATYPE.oneofs_by_name['content']
_IMAGETYPE.fields_by_name['kind'].enum_type = _IMAGETYPE_IMAGEKIND
_IMAGETYPE_IMAGEKIND.containing_type = _IMAGETYPE
_DOCUMENTTYPE.fields_by_name['kind'].enum_type = _DOCUMENTTYPE_DOCUMENTKIND
_DOCUMENTTYPE_DOCUMENTKIND.containing_type = _DOCUMENTTYPE
_VIDEOTYPE.fields_by_name['kind'].enum_type = _VIDEOTYPE_VIDEOKIND
_VIDEOTYPE_VIDEOKIND.containing_type = _VIDEOTYPE
DESCRIPTOR.message_types_by_name['MediaType'] = _MEDIATYPE
DESCRIPTOR.message_types_by_name['ImageType'] = _IMAGETYPE
DESCRIPTOR.message_types_by_name['DocumentType'] = _DOCUMENTTYPE
DESCRIPTOR.message_types_by_name['VideoType'] = _VIDEOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MediaType = _reflection.GeneratedProtocolMessageType('MediaType', (_message.Message,), dict(
  DESCRIPTOR = _MEDIATYPE,
  __module__ = 'media.MediaType_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.media.MediaType)
  ))
_sym_db.RegisterMessage(MediaType)

ImageType = _reflection.GeneratedProtocolMessageType('ImageType', (_message.Message,), dict(
  DESCRIPTOR = _IMAGETYPE,
  __module__ = 'media.MediaType_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.media.ImageType)
  ))
_sym_db.RegisterMessage(ImageType)

DocumentType = _reflection.GeneratedProtocolMessageType('DocumentType', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTTYPE,
  __module__ = 'media.MediaType_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.media.DocumentType)
  ))
_sym_db.RegisterMessage(DocumentType)

VideoType = _reflection.GeneratedProtocolMessageType('VideoType', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOTYPE,
  __module__ = 'media.MediaType_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.media.VideoType)
  ))
_sym_db.RegisterMessage(VideoType)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034io.opencannabis.schema.mediaB\rMediaItemTypeH\001P\001\242\002\003OCS'))
_MEDIATYPE.fields_by_name['kind'].has_options = True
_MEDIATYPE.fields_by_name['kind']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@@Specifies the generic kind of media being described or attached.'))
_MEDIATYPE.fields_by_name['image_type'].has_options = True
_MEDIATYPE.fields_by_name['image_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@0Specifies content for an image-based media item.'))
_MEDIATYPE.fields_by_name['document_type'].has_options = True
_MEDIATYPE.fields_by_name['document_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@2Specifies content for a document-based media item.'))
_MEDIATYPE.fields_by_name['video_type'].has_options = True
_MEDIATYPE.fields_by_name['video_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@/Specifies content for a video-based media item.'))
_IMAGETYPE.fields_by_name['kind'].has_options = True
_IMAGETYPE.fields_by_name['kind']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the format of the attached or described image.'))
_DOCUMENTTYPE.fields_by_name['kind'].has_options = True
_DOCUMENTTYPE.fields_by_name['kind']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Specifies the kind of document being attached or described.'))
_DOCUMENTTYPE.fields_by_name['compressed'].has_options = True
_DOCUMENTTYPE.fields_by_name['compressed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@=Specifies whether the attached document is compressed or not.'))
_VIDEOTYPE.fields_by_name['kind'].has_options = True
_VIDEOTYPE.fields_by_name['kind']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the kind of video being attached or described.'))
# @@protoc_insertion_point(module_scope)
