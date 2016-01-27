# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/protobuf/struct.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/google/protobuf/struct.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\"proto/google/protobuf/struct.proto\x12\x0fgoogle.protobuf\"\x84\x01\n\x06Struct\x12\x33\n\x06\x66ields\x18\x01 \x03(\x0b\x32#.google.protobuf.Struct.FieldsEntry\x1a\x45\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"\xea\x01\n\x05Value\x12\x30\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x16\n\x0cnumber_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12/\n\x0cstruct_value\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x30\n\nlist_value\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x42\x06\n\x04kind\"3\n\tListValue\x12&\n\x06values\x18\x01 \x03(\x0b\x32\x16.google.protobuf.Value*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\x42\'\n\x13\x63om.google.protobufB\x0bStructProtoP\x01\xa0\x01\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NULLVALUE = _descriptor.EnumDescriptor(
  name='NullValue',
  full_name='google.protobuf.NullValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL_VALUE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=480,
  serialized_end=507,
)
_sym_db.RegisterEnumDescriptor(_NULLVALUE)

NullValue = enum_type_wrapper.EnumTypeWrapper(_NULLVALUE)
NULL_VALUE = 0



_STRUCT_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='google.protobuf.Struct.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.protobuf.Struct.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.Struct.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=188,
)

_STRUCT = _descriptor.Descriptor(
  name='Struct',
  full_name='google.protobuf.Struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.protobuf.Struct.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STRUCT_FIELDSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=188,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='google.protobuf.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='null_value', full_name='google.protobuf.Value.null_value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_value', full_name='google.protobuf.Value.number_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.protobuf.Value.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='google.protobuf.Value.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='struct_value', full_name='google.protobuf.Value.struct_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='google.protobuf.Value.list_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='google.protobuf.Value.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=191,
  serialized_end=425,
)


_LISTVALUE = _descriptor.Descriptor(
  name='ListValue',
  full_name='google.protobuf.ListValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='google.protobuf.ListValue.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=478,
)

_STRUCT_FIELDSENTRY.fields_by_name['value'].message_type = _VALUE
_STRUCT_FIELDSENTRY.containing_type = _STRUCT
_STRUCT.fields_by_name['fields'].message_type = _STRUCT_FIELDSENTRY
_VALUE.fields_by_name['null_value'].enum_type = _NULLVALUE
_VALUE.fields_by_name['struct_value'].message_type = _STRUCT
_VALUE.fields_by_name['list_value'].message_type = _LISTVALUE
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['null_value'])
_VALUE.fields_by_name['null_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['number_value'])
_VALUE.fields_by_name['number_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['string_value'])
_VALUE.fields_by_name['string_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['bool_value'])
_VALUE.fields_by_name['bool_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['struct_value'])
_VALUE.fields_by_name['struct_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['list_value'])
_VALUE.fields_by_name['list_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_LISTVALUE.fields_by_name['values'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Struct'] = _STRUCT
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['ListValue'] = _LISTVALUE
DESCRIPTOR.enum_types_by_name['NullValue'] = _NULLVALUE

Struct = _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), dict(

  FieldsEntry = _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STRUCT_FIELDSENTRY,
    __module__ = 'proto.google.protobuf.struct_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.Struct.FieldsEntry)
    ))
  ,
  DESCRIPTOR = _STRUCT,
  __module__ = 'proto.google.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Struct)
  ))
_sym_db.RegisterMessage(Struct)
_sym_db.RegisterMessage(Struct.FieldsEntry)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'proto.google.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Value)
  ))
_sym_db.RegisterMessage(Value)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), dict(
  DESCRIPTOR = _LISTVALUE,
  __module__ = 'proto.google.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.ListValue)
  ))
_sym_db.RegisterMessage(ListValue)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.google.protobufB\013StructProtoP\001\240\001\001'))
_STRUCT_FIELDSENTRY.has_options = True
_STRUCT_FIELDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
