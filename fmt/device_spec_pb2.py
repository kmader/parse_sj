# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gadget_info_pb2 as gadget__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_spec.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x64\x65vice_spec.proto\x12\x06goosci\x1a\x11gadget_info.proto\"<\n\nDeviceSpec\x12 \n\x04info\x18\x01 \x01(\x0b\x32\x12.goosci.GadgetInfo\x12\x0c\n\x04name\x18\x02 \x01(\tBO\n3com.google.android.apps.forscience.whistlepunk.dataB\x10GoosciDeviceSpecH\x03\xa2\x02\x03GSJ')
  ,
  dependencies=[gadget__info__pb2.DESCRIPTOR,])




_DEVICESPEC = _descriptor.Descriptor(
  name='DeviceSpec',
  full_name='goosci.DeviceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='goosci.DeviceSpec.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='goosci.DeviceSpec.name', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=108,
)

_DEVICESPEC.fields_by_name['info'].message_type = gadget__info__pb2._GADGETINFO
DESCRIPTOR.message_types_by_name['DeviceSpec'] = _DEVICESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceSpec = _reflection.GeneratedProtocolMessageType('DeviceSpec', (_message.Message,), dict(
  DESCRIPTOR = _DEVICESPEC,
  __module__ = 'device_spec_pb2'
  # @@protoc_insertion_point(class_scope:goosci.DeviceSpec)
  ))
_sym_db.RegisterMessage(DeviceSpec)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n3com.google.android.apps.forscience.whistlepunk.dataB\020GoosciDeviceSpecH\003\242\002\003GSJ'))
# @@protoc_insertion_point(module_scope)
