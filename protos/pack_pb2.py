# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pack.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import celaut_pb2 as celaut__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\npack.proto\x12\x07\x63ompile\x1a\x0c\x63\x65laut.proto\"\x8e\x06\n\x07Service\x12\r\n\x05prose\x18\x01 \x01(\t\x12-\n\tcontainer\x18\x02 \x01(\x0b\x32\x1a.compile.Service.Container\x12 \n\x03\x61pi\x18\x03 \x01(\x0b\x32\x13.celaut.Service.Api\x12(\n\x07network\x18\x04 \x03(\x0b\x32\x17.celaut.Service.Network\x1a\xf8\x04\n\tContainer\x12<\n\x0c\x61rchitecture\x18\x01 \x01(\x0b\x32&.celaut.Service.Container.Architecture\x12\x38\n\nfilesystem\x18\x02 \x01(\x0b\x32$.celaut.Service.Container.Filesystem\x12Q\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x33.compile.Service.Container.EnviromentVariablesEntry\x12\x12\n\nentrypoint\x18\x04 \x03(\t\x12\x30\n\x06\x63onfig\x18\x05 \x01(\x0b\x32 .celaut.Service.Container.Config\x12\x39\n\x13node_protocol_stack\x18\x06 \x03(\x0b\x32\x1c.celaut.Service.Api.Protocol\x1a\xce\x01\n\nFilesystem\x12@\n\x06\x62ranch\x18\x01 \x03(\x0b\x32\x30.compile.Service.Container.Filesystem.ItemBranch\x1a~\n\nItemBranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x04\x66ile\x18\x02 \x01(\x0cH\x00\x12\x0e\n\x04link\x18\x03 \x01(\tH\x00\x12:\n\nfilesystem\x18\x04 \x01(\x0b\x32$.celaut.Service.Container.FilesystemH\x00\x42\x06\n\x04item\x1aN\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.celaut.DataFormat:\x02\x38\x01\"!\n\x13PackOutputServiceId\x12\n\n\x02id\x18\x01 \x01(\x0c\"\"\n\x0fPackOutputError\x12\x0f\n\x07message\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pack_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._options = None
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _globals['_SERVICE']._serialized_start=38
  _globals['_SERVICE']._serialized_end=820
  _globals['_SERVICE_CONTAINER']._serialized_start=188
  _globals['_SERVICE_CONTAINER']._serialized_end=820
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_start=534
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_end=740
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_start=614
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_end=740
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_start=742
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_end=820
  _globals['_PACKOUTPUTSERVICEID']._serialized_start=822
  _globals['_PACKOUTPUTSERVICEID']._serialized_end=855
  _globals['_PACKOUTPUTERROR']._serialized_start=857
  _globals['_PACKOUTPUTERROR']._serialized_end=891
# @@protoc_insertion_point(module_scope)
