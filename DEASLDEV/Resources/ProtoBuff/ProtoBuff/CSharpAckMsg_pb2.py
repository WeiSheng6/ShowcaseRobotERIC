# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2


_CSHARPACKMSG_SENSORTYPE = descriptor.EnumDescriptor(
  name='SensorType',
  full_name='LTLMoPCsharpInterface.CSharpAckMsg.SensorType',
  filename='SensorType',
  values=[
    descriptor.EnumValueDescriptor(
      name='LIDAR', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ARTAG', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)


_CSHARPACKMSG_SENSOR = descriptor.Descriptor(
  name='Sensor',
  full_name='LTLMoPCsharpInterface.CSharpAckMsg.Sensor',
  filename='CSharpAckMsg.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='LTLMoPCsharpInterface.CSharpAckMsg.Sensor.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stat', full_name='LTLMoPCsharpInterface.CSharpAckMsg.Sensor.stat', index=1,
      number=2, type=1, cpp_type=5, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='LTLMoPCsharpInterface.CSharpAckMsg.Sensor.data', index=2,
      number=3, type=1, cpp_type=5, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_CSHARPACKMSG = descriptor.Descriptor(
  name='CSharpAckMsg',
  full_name='LTLMoPCsharpInterface.CSharpAckMsg',
  filename='CSharpAckMsg.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='LTLMoPCsharpInterface.CSharpAckMsg.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='LTLMoPCsharpInterface.CSharpAckMsg.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msg', full_name='LTLMoPCsharpInterface.CSharpAckMsg.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s1', full_name='LTLMoPCsharpInterface.CSharpAckMsg.s1', index=3,
      number=16, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s2', full_name='LTLMoPCsharpInterface.CSharpAckMsg.s2', index=4,
      number=17, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s3', full_name='LTLMoPCsharpInterface.CSharpAckMsg.s3', index=5,
      number=18, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s4', full_name='LTLMoPCsharpInterface.CSharpAckMsg.s4', index=6,
      number=19, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s5', full_name='LTLMoPCsharpInterface.CSharpAckMsg.s5', index=7,
      number=20, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _CSHARPACKMSG_SENSORTYPE,
  ],
  options=None)


_CSHARPACKMSG_SENSOR.fields_by_name['type'].enum_type = _CSHARPACKMSG_SENSORTYPE
_CSHARPACKMSG.fields_by_name['s1'].message_type = _CSHARPACKMSG_SENSOR
_CSHARPACKMSG.fields_by_name['s2'].message_type = _CSHARPACKMSG_SENSOR
_CSHARPACKMSG.fields_by_name['s3'].message_type = _CSHARPACKMSG_SENSOR
_CSHARPACKMSG.fields_by_name['s4'].message_type = _CSHARPACKMSG_SENSOR
_CSHARPACKMSG.fields_by_name['s5'].message_type = _CSHARPACKMSG_SENSOR

class CSharpAckMsg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Sensor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CSHARPACKMSG_SENSOR
  DESCRIPTOR = _CSHARPACKMSG

