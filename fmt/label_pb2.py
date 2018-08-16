# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import caption_pb2 as caption__pb2
import label_value_pb2 as label__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='label.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\x0blabel.proto\x12\x06goosci\x1a\rcaption.proto\x1a\x11label_value.proto\"\xe7\x01\n\x05Label\x12\x0f\n\x07labelId\x18\x01 \x01(\t\x12\x13\n\x0btimestampMs\x18\x02 \x01(\x03\x12\x16\n\x0e\x63reationTimeMs\x18\x03 \x01(\x03\x12 \n\x07\x63\x61ption\x18\x04 \x01(\x0b\x32\x0f.goosci.Caption\x12%\n\x04type\x18\x05 \x01(\x0e\x32\x17.goosci.Label.ValueType\x12\x11\n\tprotoData\x18\x06 \x01(\x0c\"D\n\tValueType\x12\x08\n\x04TEXT\x10\x01\x12\x0b\n\x07PICTURE\x10\x02\x12\x12\n\x0eSENSOR_TRIGGER\x10\x03\x12\x0c\n\x08SNAPSHOT\x10\x04\x42N\n7com.google.android.apps.forscience.whistlepunk.metadataB\x0bGoosciLabelH\x03\xa2\x02\x03GSJ')
  ,
  dependencies=[caption__pb2.DESCRIPTOR,label__value__pb2.DESCRIPTOR,])



_LABEL_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='goosci.Label.ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICTURE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TRIGGER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNAPSHOT', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=221,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_LABEL_VALUETYPE)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='goosci.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labelId', full_name='goosci.Label.labelId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestampMs', full_name='goosci.Label.timestampMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creationTimeMs', full_name='goosci.Label.creationTimeMs', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='caption', full_name='goosci.Label.caption', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='goosci.Label.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protoData', full_name='goosci.Label.protoData', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LABEL_VALUETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=289,
)

_LABEL.fields_by_name['caption'].message_type = caption__pb2._CAPTION
_LABEL.fields_by_name['type'].enum_type = _LABEL_VALUETYPE
_LABEL_VALUETYPE.containing_type = _LABEL
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
  DESCRIPTOR = _LABEL,
  __module__ = 'label_pb2'
  # @@protoc_insertion_point(class_scope:goosci.Label)
  ))
_sym_db.RegisterMessage(Label)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n7com.google.android.apps.forscience.whistlepunk.metadataB\013GoosciLabelH\003\242\002\003GSJ'))
# @@protoc_insertion_point(module_scope)
