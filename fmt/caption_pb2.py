# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caption.proto

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
  name='caption.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\rcaption.proto\x12\x06goosci\"4\n\x07\x43\x61ption\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1b\n\x13lastEditedTimestamp\x18\x02 \x01(\x03\x42P\n7com.google.android.apps.forscience.whistlepunk.metadataB\rGoosciCaptionH\x03\xa2\x02\x03GSJ')
)




_CAPTION = _descriptor.Descriptor(
  name='Caption',
  full_name='goosci.Caption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='goosci.Caption.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastEditedTimestamp', full_name='goosci.Caption.lastEditedTimestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['Caption'] = _CAPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Caption = _reflection.GeneratedProtocolMessageType('Caption', (_message.Message,), dict(
  DESCRIPTOR = _CAPTION,
  __module__ = 'caption_pb2'
  # @@protoc_insertion_point(class_scope:goosci.Caption)
  ))
_sym_db.RegisterMessage(Caption)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n7com.google.android.apps.forscience.whistlepunk.metadataB\rGoosciCaptionH\003\242\002\003GSJ'))
# @@protoc_insertion_point(module_scope)