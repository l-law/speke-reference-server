# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pssh.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pssh.proto',
  package='shaka.media',
  syntax='proto2',
  serialized_pb=_b('\n\npssh.proto\x12\x0bshaka.media\"\xa3\x02\n\x10WidevinePsshData\x12:\n\talgorithm\x18\x01 \x01(\x0e\x32\'.shaka.media.WidevinePsshData.Algorithm\x12\x0e\n\x06key_id\x18\x02 \x03(\x0c\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x12\n\ncontent_id\x18\x04 \x01(\x0c\x12\x12\n\ntrack_type\x18\x05 \x01(\t\x12\x0e\n\x06policy\x18\x06 \x01(\t\x12\x1b\n\x13\x63rypto_period_index\x18\x07 \x01(\r\x12\x17\n\x0fgrouped_license\x18\x08 \x01(\x0c\x12\x19\n\x11protection_scheme\x18\t \x01(\r\"(\n\tAlgorithm\x12\x0f\n\x0bUNENCRYPTED\x10\x00\x12\n\n\x06\x41\x45SCTR\x10\x01\"G\n\x0eWidevineHeader\x12\x0f\n\x07key_ids\x18\x02 \x03(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x12\n\ncontent_id\x18\x04 \x01(\x0c')
)



_WIDEVINEPSSHDATA_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='shaka.media.WidevinePsshData.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNENCRYPTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AESCTR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=279,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_WIDEVINEPSSHDATA_ALGORITHM)


_WIDEVINEPSSHDATA = _descriptor.Descriptor(
  name='WidevinePsshData',
  full_name='shaka.media.WidevinePsshData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='shaka.media.WidevinePsshData.algorithm', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='shaka.media.WidevinePsshData.key_id', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider', full_name='shaka.media.WidevinePsshData.provider', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_id', full_name='shaka.media.WidevinePsshData.content_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_type', full_name='shaka.media.WidevinePsshData.track_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='shaka.media.WidevinePsshData.policy', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypto_period_index', full_name='shaka.media.WidevinePsshData.crypto_period_index', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grouped_license', full_name='shaka.media.WidevinePsshData.grouped_license', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protection_scheme', full_name='shaka.media.WidevinePsshData.protection_scheme', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WIDEVINEPSSHDATA_ALGORITHM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=319,
)


_WIDEVINEHEADER = _descriptor.Descriptor(
  name='WidevineHeader',
  full_name='shaka.media.WidevineHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_ids', full_name='shaka.media.WidevineHeader.key_ids', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider', full_name='shaka.media.WidevineHeader.provider', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_id', full_name='shaka.media.WidevineHeader.content_id', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=392,
)

_WIDEVINEPSSHDATA.fields_by_name['algorithm'].enum_type = _WIDEVINEPSSHDATA_ALGORITHM
_WIDEVINEPSSHDATA_ALGORITHM.containing_type = _WIDEVINEPSSHDATA
DESCRIPTOR.message_types_by_name['WidevinePsshData'] = _WIDEVINEPSSHDATA
DESCRIPTOR.message_types_by_name['WidevineHeader'] = _WIDEVINEHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WidevinePsshData = _reflection.GeneratedProtocolMessageType('WidevinePsshData', (_message.Message,), dict(
  DESCRIPTOR = _WIDEVINEPSSHDATA,
  __module__ = 'pssh_pb2'
  # @@protoc_insertion_point(class_scope:shaka.media.WidevinePsshData)
  ))
_sym_db.RegisterMessage(WidevinePsshData)

WidevineHeader = _reflection.GeneratedProtocolMessageType('WidevineHeader', (_message.Message,), dict(
  DESCRIPTOR = _WIDEVINEHEADER,
  __module__ = 'pssh_pb2'
  # @@protoc_insertion_point(class_scope:shaka.media.WidevineHeader)
  ))
_sym_db.RegisterMessage(WidevineHeader)


# @@protoc_insertion_point(module_scope)
