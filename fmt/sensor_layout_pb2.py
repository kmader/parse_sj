# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_layout.proto

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
  name='sensor_layout.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\x13sensor_layout.proto\x12\x06goosci\"\x9c\x03\n\x0cSensorLayout\x12\x10\n\x08sensorId\x18\x01 \x01(\t\x12\x36\n\x08\x63\x61rdView\x18\x02 \x01(\x0e\x32\x1d.goosci.SensorLayout.CardView:\x05METER\x12\x1b\n\x0c\x61udioEnabled\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10showStatsOverlay\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05\x63olor\x18\x05 \x01(\x05:\x01\x30\x42\x02\x18\x01\x12\x30\n\x06\x65xtras\x18\x06 \x03(\x0b\x32 .goosci.SensorLayout.ExtrasEntry\x12\x19\n\x11minimumYAxisValue\x18\x07 \x01(\x01\x12\x19\n\x11maximumYAxisValue\x18\x08 \x01(\x01\x12\x1e\n\x16\x61\x63tiveSensorTriggerIds\x18\t \x03(\t\x12\x15\n\ncolorIndex\x18\n \x01(\x05:\x01\x30\x1a-\n\x0b\x45xtrasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\" \n\x08\x43\x61rdView\x12\t\n\x05METER\x10\x01\x12\t\n\x05GRAPH\x10\x02\x42Q\n3com.google.android.apps.forscience.whistlepunk.dataB\x12GoosciSensorLayoutH\x03\xa2\x02\x03GSJ')
)



_SENSORLAYOUT_CARDVIEW = _descriptor.EnumDescriptor(
  name='CardView',
  full_name='goosci.SensorLayout.CardView',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAPH', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=412,
  serialized_end=444,
)
_sym_db.RegisterEnumDescriptor(_SENSORLAYOUT_CARDVIEW)


_SENSORLAYOUT_EXTRASENTRY = _descriptor.Descriptor(
  name='ExtrasEntry',
  full_name='goosci.SensorLayout.ExtrasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='goosci.SensorLayout.ExtrasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='goosci.SensorLayout.ExtrasEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=410,
)

_SENSORLAYOUT = _descriptor.Descriptor(
  name='SensorLayout',
  full_name='goosci.SensorLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorId', full_name='goosci.SensorLayout.sensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardView', full_name='goosci.SensorLayout.cardView', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioEnabled', full_name='goosci.SensorLayout.audioEnabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showStatsOverlay', full_name='goosci.SensorLayout.showStatsOverlay', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='goosci.SensorLayout.color', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extras', full_name='goosci.SensorLayout.extras', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimumYAxisValue', full_name='goosci.SensorLayout.minimumYAxisValue', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximumYAxisValue', full_name='goosci.SensorLayout.maximumYAxisValue', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activeSensorTriggerIds', full_name='goosci.SensorLayout.activeSensorTriggerIds', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colorIndex', full_name='goosci.SensorLayout.colorIndex', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SENSORLAYOUT_EXTRASENTRY, ],
  enum_types=[
    _SENSORLAYOUT_CARDVIEW,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=444,
)

_SENSORLAYOUT_EXTRASENTRY.containing_type = _SENSORLAYOUT
_SENSORLAYOUT.fields_by_name['cardView'].enum_type = _SENSORLAYOUT_CARDVIEW
_SENSORLAYOUT.fields_by_name['extras'].message_type = _SENSORLAYOUT_EXTRASENTRY
_SENSORLAYOUT_CARDVIEW.containing_type = _SENSORLAYOUT
DESCRIPTOR.message_types_by_name['SensorLayout'] = _SENSORLAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorLayout = _reflection.GeneratedProtocolMessageType('SensorLayout', (_message.Message,), dict(

  ExtrasEntry = _reflection.GeneratedProtocolMessageType('ExtrasEntry', (_message.Message,), dict(
    DESCRIPTOR = _SENSORLAYOUT_EXTRASENTRY,
    __module__ = 'sensor_layout_pb2'
    # @@protoc_insertion_point(class_scope:goosci.SensorLayout.ExtrasEntry)
    ))
  ,
  DESCRIPTOR = _SENSORLAYOUT,
  __module__ = 'sensor_layout_pb2'
  # @@protoc_insertion_point(class_scope:goosci.SensorLayout)
  ))
_sym_db.RegisterMessage(SensorLayout)
_sym_db.RegisterMessage(SensorLayout.ExtrasEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n3com.google.android.apps.forscience.whistlepunk.dataB\022GoosciSensorLayoutH\003\242\002\003GSJ'))
_SENSORLAYOUT_EXTRASENTRY.has_options = True
_SENSORLAYOUT_EXTRASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SENSORLAYOUT.fields_by_name['color'].has_options = True
_SENSORLAYOUT.fields_by_name['color']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
