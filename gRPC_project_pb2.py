# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC_project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gRPC_project.proto',
  package='gRPC_project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12gRPC_project.proto\x12\x0cgRPC_project\"\"\n\x03Key\x12\x0e\n\x06key_id\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t2@\n\rsetKeyService\x12/\n\x07set_key\x12\x11.gRPC_project.Key\x1a\x11.gRPC_project.Key2@\n\rgetKeyService\x12/\n\x07get_key\x12\x11.gRPC_project.Key\x1a\x11.gRPC_project.Keyb\x06proto3'
)




_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='gRPC_project.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='gRPC_project.Key.key_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='gRPC_project.Key.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['Key'] = _KEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'gRPC_project_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_project.Key)
  })
_sym_db.RegisterMessage(Key)



_SETKEYSERVICE = _descriptor.ServiceDescriptor(
  name='setKeyService',
  full_name='gRPC_project.setKeyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=72,
  serialized_end=136,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_key',
    full_name='gRPC_project.setKeyService.set_key',
    index=0,
    containing_service=None,
    input_type=_KEY,
    output_type=_KEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SETKEYSERVICE)

DESCRIPTOR.services_by_name['setKeyService'] = _SETKEYSERVICE


_GETKEYSERVICE = _descriptor.ServiceDescriptor(
  name='getKeyService',
  full_name='gRPC_project.getKeyService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=138,
  serialized_end=202,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_key',
    full_name='gRPC_project.getKeyService.get_key',
    index=0,
    containing_service=None,
    input_type=_KEY,
    output_type=_KEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETKEYSERVICE)

DESCRIPTOR.services_by_name['getKeyService'] = _GETKEYSERVICE

# @@protoc_insertion_point(module_scope)
