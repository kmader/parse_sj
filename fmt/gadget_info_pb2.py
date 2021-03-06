# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gadget_info.proto

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
  name='gadget_info.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\x11gadget_info.proto\x12\x06goosci\"\xab\x01\n\nGadgetInfo\x12-\n\x08platform\x18\x01 \x01(\x0e\x32\x1b.goosci.GadgetInfo.Platform\x12\x12\n\nproviderId\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0e\n\x06hostId\x18\x04 \x01(\t\x12\x17\n\x0fhostDescription\x18\x05 \x01(\t\" \n\x08Platform\x12\x0b\n\x07\x41NDROID\x10\x00\x12\x07\n\x03IOS\x10\x01\x42O\n3com.google.android.apps.forscience.whistlepunk.dataB\x10GoosciGadgetInfoH\x03\xa2\x02\x03GSJ')
)



_GADGETINFO_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='goosci.GadgetInfo.Platform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANDROID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=169,
  serialized_end=201,
)
_sym_db.RegisterEnumDescriptor(_GADGETINFO_PLATFORM)


_GADGETINFO = _descriptor.Descriptor(
  name='GadgetInfo',
  full_name='goosci.GadgetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='goosci.GadgetInfo.platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providerId', full_name='goosci.GadgetInfo.providerId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='goosci.GadgetInfo.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostId', full_name='goosci.GadgetInfo.hostId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostDescription', full_name='goosci.GadgetInfo.hostDescription', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GADGETINFO_PLATFORM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=201,
)

_GADGETINFO.fields_by_name['platform'].enum_type = _GADGETINFO_PLATFORM
_GADGETINFO_PLATFORM.containing_type = _GADGETINFO
DESCRIPTOR.message_types_by_name['GadgetInfo'] = _GADGETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GadgetInfo = _reflection.GeneratedProtocolMessageType('GadgetInfo', (_message.Message,), dict(
  DESCRIPTOR = _GADGETINFO,
  __module__ = 'gadget_info_pb2'
  # @@protoc_insertion_point(class_scope:goosci.GadgetInfo)
  ))
_sym_db.RegisterMessage(GadgetInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n3com.google.android.apps.forscience.whistlepunk.dataB\020GoosciGadgetInfoH\003\242\002\003GSJ'))
# @@protoc_insertion_point(module_scope)
