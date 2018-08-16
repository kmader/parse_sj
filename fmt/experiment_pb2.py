# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import label_pb2 as label__pb2
import trial_pb2 as trial__pb2
import sensor_layout_pb2 as sensor__layout__pb2
import sensor_trigger_pb2 as sensor__trigger__pb2
import sensor_spec_pb2 as sensor__spec__pb2
import version_pb2 as version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='experiment.proto',
  package='goosci',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x65xperiment.proto\x12\x06goosci\x1a\x0blabel.proto\x1a\x0btrial.proto\x1a\x13sensor_layout.proto\x1a\x14sensor_trigger.proto\x1a\x11sensor_spec.proto\x1a\rversion.proto\"\x90\x04\n\nExperiment\x12\x16\n\x0e\x63reationTimeMs\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x17\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x02\x18\x01\x12+\n\rsensorLayouts\x18\x04 \x03(\x0b\x32\x14.goosci.SensorLayout\x12\x1d\n\x06trials\x18\x05 \x03(\x0b\x32\r.goosci.Trial\x12\x1d\n\x06labels\x18\x06 \x03(\x0b\x32\r.goosci.Label\x12\x37\n\x11\x65xperimentSensors\x18\x07 \x03(\x0b\x32\x18.goosci.ExperimentSensorB\x02\x18\x01\x12-\n\x0esensorTriggers\x18\x08 \x03(\x0b\x32\x15.goosci.SensorTrigger\x12\x16\n\x07version\x18\t \x01(\x05:\x01\x31\x42\x02\x18\x01\x12\x1b\n\x0cminorVersion\x18\n \x01(\x05:\x01\x31\x42\x02\x18\x01\x12\x38\n\x10\x61vailableSensors\x18\x0b \x03(\x0b\x32\x1e.goosci.Experiment.SensorEntry\x12(\n\x0b\x66ileVersion\x18\x0c \x01(\x0b\x32\x13.goosci.FileVersion\x12\x13\n\x0btotalTrials\x18\r \x01(\x05\x1a\x41\n\x0bSensorEntry\x12\x10\n\x08sensorId\x18\x01 \x01(\t\x12 \n\x04spec\x18\x02 \x01(\x0b\x32\x12.goosci.SensorSpec\"6\n\x10\x45xperimentSensor\x12\x10\n\x08sensorId\x18\x01 \x01(\t\x12\x10\n\x08included\x18\x02 \x01(\x08\x42S\n7com.google.android.apps.forscience.whistlepunk.metadataB\x10GoosciExperimentH\x03\xa2\x02\x03GSJ')
  ,
  dependencies=[label__pb2.DESCRIPTOR,trial__pb2.DESCRIPTOR,sensor__layout__pb2.DESCRIPTOR,sensor__trigger__pb2.DESCRIPTOR,sensor__spec__pb2.DESCRIPTOR,version__pb2.DESCRIPTOR,])




_EXPERIMENT_SENSORENTRY = _descriptor.Descriptor(
  name='SensorEntry',
  full_name='goosci.Experiment.SensorEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorId', full_name='goosci.Experiment.SensorEntry.sensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='goosci.Experiment.SensorEntry.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=660,
)

_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='goosci.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creationTimeMs', full_name='goosci.Experiment.creationTimeMs', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='goosci.Experiment.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='goosci.Experiment.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorLayouts', full_name='goosci.Experiment.sensorLayouts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trials', full_name='goosci.Experiment.trials', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='goosci.Experiment.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experimentSensors', full_name='goosci.Experiment.experimentSensors', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorTriggers', full_name='goosci.Experiment.sensorTriggers', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='goosci.Experiment.version', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minorVersion', full_name='goosci.Experiment.minorVersion', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availableSensors', full_name='goosci.Experiment.availableSensors', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileVersion', full_name='goosci.Experiment.fileVersion', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalTrials', full_name='goosci.Experiment.totalTrials', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXPERIMENT_SENSORENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=660,
)


_EXPERIMENTSENSOR = _descriptor.Descriptor(
  name='ExperimentSensor',
  full_name='goosci.ExperimentSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorId', full_name='goosci.ExperimentSensor.sensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='included', full_name='goosci.ExperimentSensor.included', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=716,
)

_EXPERIMENT_SENSORENTRY.fields_by_name['spec'].message_type = sensor__spec__pb2._SENSORSPEC
_EXPERIMENT_SENSORENTRY.containing_type = _EXPERIMENT
_EXPERIMENT.fields_by_name['sensorLayouts'].message_type = sensor__layout__pb2._SENSORLAYOUT
_EXPERIMENT.fields_by_name['trials'].message_type = trial__pb2._TRIAL
_EXPERIMENT.fields_by_name['labels'].message_type = label__pb2._LABEL
_EXPERIMENT.fields_by_name['experimentSensors'].message_type = _EXPERIMENTSENSOR
_EXPERIMENT.fields_by_name['sensorTriggers'].message_type = sensor__trigger__pb2._SENSORTRIGGER
_EXPERIMENT.fields_by_name['availableSensors'].message_type = _EXPERIMENT_SENSORENTRY
_EXPERIMENT.fields_by_name['fileVersion'].message_type = version__pb2._FILEVERSION
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['ExperimentSensor'] = _EXPERIMENTSENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(

  SensorEntry = _reflection.GeneratedProtocolMessageType('SensorEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXPERIMENT_SENSORENTRY,
    __module__ = 'experiment_pb2'
    # @@protoc_insertion_point(class_scope:goosci.Experiment.SensorEntry)
    ))
  ,
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:goosci.Experiment)
  ))
_sym_db.RegisterMessage(Experiment)
_sym_db.RegisterMessage(Experiment.SensorEntry)

ExperimentSensor = _reflection.GeneratedProtocolMessageType('ExperimentSensor', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTSENSOR,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:goosci.ExperimentSensor)
  ))
_sym_db.RegisterMessage(ExperimentSensor)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n7com.google.android.apps.forscience.whistlepunk.metadataB\020GoosciExperimentH\003\242\002\003GSJ'))
_EXPERIMENT.fields_by_name['description'].has_options = True
_EXPERIMENT.fields_by_name['description']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_EXPERIMENT.fields_by_name['experimentSensors'].has_options = True
_EXPERIMENT.fields_by_name['experimentSensors']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_EXPERIMENT.fields_by_name['version'].has_options = True
_EXPERIMENT.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_EXPERIMENT.fields_by_name['minorVersion'].has_options = True
_EXPERIMENT.fields_by_name['minorVersion']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
