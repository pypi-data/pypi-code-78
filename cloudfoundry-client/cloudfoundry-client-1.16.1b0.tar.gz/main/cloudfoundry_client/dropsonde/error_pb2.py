# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: error.proto

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
  name='error.proto',
  package='cloudfoundry.dropsonde',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x65rror.proto\x12\x16\x63loudfoundry.dropsonde\"6\n\x05\x45rror\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x0c\n\x04\x63ode\x18\x02 \x02(\x05\x12\x0f\n\x07message\x18\x03 \x02(\tB1\n!org.cloudfoundry.dropsonde.eventsB\x0c\x45rrorFactory')
)




_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='cloudfoundry.dropsonde.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='cloudfoundry.dropsonde.Error.source', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='cloudfoundry.dropsonde.Error.code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cloudfoundry.dropsonde.Error.message', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=39,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'error_pb2'
  # @@protoc_insertion_point(class_scope:cloudfoundry.dropsonde.Error)
  ))
_sym_db.RegisterMessage(Error)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!org.cloudfoundry.dropsonde.eventsB\014ErrorFactory'))
# @@protoc_insertion_point(module_scope)
