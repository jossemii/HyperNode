# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: celaut.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x65laut.proto\x12\x06\x63\x65laut\"\xe5\x04\n\x08\x46ieldDef\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x1b.celaut.FieldDef.MessageDefH\x00\x12\x32\n\tprimitive\x18\x02 \x01(\x0b\x32\x1d.celaut.FieldDef.PrimitiveDefH\x00\x12(\n\x04\x65num\x18\x03 \x01(\x0b\x32\x18.celaut.FieldDef.EnumDefH\x00\x1a,\n\x0cPrimitiveDef\x12\x12\n\x05regex\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_regex\x1ak\n\x07\x45numDef\x12\x32\n\x05value\x18\x01 \x03(\x0b\x32#.celaut.FieldDef.EnumDef.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\xa6\x02\n\nMessageDef\x12\x35\n\x05param\x18\x01 \x03(\x0b\x32&.celaut.FieldDef.MessageDef.ParamEntry\x12\x33\n\x05oneof\x18\x02 \x03(\x0b\x32$.celaut.FieldDef.MessageDef.OneofDef\x1a=\n\x08ParamDef\x12\x1f\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x10.celaut.FieldDef\x12\x10\n\x08repeated\x18\x02 \x01(\x08\x1a\x19\n\x08OneofDef\x12\r\n\x05index\x18\x01 \x03(\x05\x1aR\n\nParamEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.celaut.FieldDef.MessageDef.ParamDef:\x02\x38\x01\x42\x07\n\x05value\"I\n\x0e\x43ontractLedger\x12\x10\n\x08\x63ontract\x18\x01 \x01(\x0c\x12\x15\n\rcontract_addr\x18\x02 \x01(\t\x12\x0e\n\x06ledger\x18\x03 \x01(\t\"\x97\x03\n\x08Metadata\x12.\n\x07hashtag\x18\x01 \x01(\x0b\x32\x18.celaut.Metadata.HashTagH\x00\x88\x01\x01\x12%\n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDefH\x01\x88\x01\x01\x12\x31\n\x11reputation_proofs\x18\x03 \x03(\x0b\x32\x16.celaut.ContractLedger\x1a\xe9\x01\n\x07HashTag\x12+\n\x04hash\x18\x01 \x03(\x0b\x32\x1d.celaut.Metadata.HashTag.Hash\x12\x0b\n\x03tag\x18\x02 \x03(\t\x12:\n\x0c\x61ttr_hashtag\x18\x03 \x03(\x0b\x32$.celaut.Metadata.HashTag.AttrHashTag\x1a#\n\x04Hash\x12\x0c\n\x04type\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x1a\x43\n\x0b\x41ttrHashTag\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\'\n\x05value\x18\x02 \x03(\x0b\x32\x18.celaut.Metadata.HashTagB\n\n\x08_hashtagB\t\n\x07_format\"\xcd\x01\n\x06\x41ppDef\x12*\n\x06method\x18\x01 \x03(\x0b\x32\x1a.celaut.AppDef.MethodEntry\x1aN\n\tMethodDef\x12\x1f\n\x05input\x18\x01 \x01(\x0b\x32\x10.celaut.FieldDef\x12 \n\x06output\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef\x1aG\n\x0bMethodEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.celaut.AppDef.MethodDef:\x02\x38\x01\"\xab\t\n\x07Service\x12\r\n\x05prose\x18\x01 \x01(\t\x12,\n\tcontainer\x18\x02 \x01(\x0b\x32\x19.celaut.Service.Container\x12 \n\x03\x61pi\x18\x03 \x01(\x0b\x32\x13.celaut.Service.Api\x12(\n\x07network\x18\x04 \x03(\x0b\x32\x17.celaut.Service.Network\x1a\xe5\x01\n\x03\x41pi\x12&\n\x04slot\x18\x02 \x03(\x0b\x32\x18.celaut.Service.Api.Slot\x12\x31\n\x11payment_contracts\x18\x03 \x03(\x0b\x32\x16.celaut.ContractLedger\x1a\x37\n\x08Protocol\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\r\n\x05prose\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormal\x18\x03 \x01(\x0c\x1aJ\n\x04Slot\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x34\n\x0eprotocol_stack\x18\x02 \x03(\x0b\x32\x1c.celaut.Service.Api.Protocol\x1a\xf6\x05\n\tContainer\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\x0c\x12\x12\n\nfilesystem\x18\x02 \x01(\x0c\x12P\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x32.celaut.Service.Container.EnviromentVariablesEntry\x12\x12\n\nentrypoint\x18\x04 \x03(\t\x12\x30\n\x06\x63onfig\x18\x05 \x01(\x0b\x32 .celaut.Service.Container.Config\x12\x39\n\x13node_protocol_stack\x18\x06 \x03(\x0b\x32\x1c.celaut.Service.Api.Protocol\x1a;\n\x0c\x41rchitecture\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\r\n\x05prose\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormal\x18\x03 \x01(\x0c\x1a\xa6\x02\n\nFilesystem\x12?\n\x06\x62ranch\x18\x01 \x03(\x0b\x32/.celaut.Service.Container.Filesystem.ItemBranch\x1a\xd6\x01\n\nItemBranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x04\x66ile\x18\x02 \x01(\x0cH\x00\x12\x44\n\x04link\x18\x03 \x01(\x0b\x32\x34.celaut.Service.Container.Filesystem.ItemBranch.LinkH\x00\x12:\n\nfilesystem\x18\x04 \x01(\x0b\x32$.celaut.Service.Container.FilesystemH\x00\x1a \n\x04Link\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0b\n\x03\x64st\x18\x02 \x01(\tB\x06\n\x04item\x1a\x38\n\x06\x43onfig\x12\x0c\n\x04path\x18\x01 \x03(\t\x12 \n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef\x1aL\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef:\x02\x38\x01\x1a\x36\n\x07Network\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\r\n\x05prose\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormal\x18\x03 \x01(\x0c\"\xc0\x01\n\x08Instance\x12 \n\x03\x61pi\x18\x01 \x01(\x0b\x32\x13.celaut.Service.Api\x12+\n\x08uri_slot\x18\x02 \x03(\x0b\x32\x19.celaut.Instance.Uri_Slot\x1a\x1f\n\x03Uri\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\x44\n\x08Uri_Slot\x12\x15\n\rinternal_port\x18\x01 \x01(\x05\x12!\n\x03uri\x18\x02 \x03(\x0b\x32\x14.celaut.Instance.Uri\"\xac\x01\n\rConfiguration\x12L\n\x14\x65nviroment_variables\x18\x01 \x03(\x0b\x32..celaut.Configuration.EnviromentVariablesEntry\x12\x11\n\tspec_slot\x18\x02 \x03(\x05\x1a:\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x91\x01\n\x11\x43onfigurationFile\x12!\n\x07gateway\x18\x01 \x01(\x0b\x32\x10.celaut.Instance\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.celaut.Configuration\x12\x32\n\x14initial_sysresources\x18\x03 \x01(\x0b\x32\x14.celaut.Sysresources\"\xd6\x01\n\x0cSysresources\x12\x19\n\x0c\x62lkio_weight\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x17\n\ncpu_period\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x16\n\tcpu_quota\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tmem_limit\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x17\n\ndisk_space\x18\x05 \x01(\x04H\x04\x88\x01\x01\x42\x0f\n\r_blkio_weightB\r\n\x0b_cpu_periodB\x0c\n\n_cpu_quotaB\x0c\n\n_mem_limitB\r\n\x0b_disk_spaceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'celaut_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FIELDDEF_ENUMDEF_VALUEENTRY._options = None
  _FIELDDEF_ENUMDEF_VALUEENTRY._serialized_options = b'8\001'
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._options = None
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._serialized_options = b'8\001'
  _APPDEF_METHODENTRY._options = None
  _APPDEF_METHODENTRY._serialized_options = b'8\001'
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._options = None
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._options = None
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _globals['_FIELDDEF']._serialized_start=25
  _globals['_FIELDDEF']._serialized_end=638
  _globals['_FIELDDEF_PRIMITIVEDEF']._serialized_start=179
  _globals['_FIELDDEF_PRIMITIVEDEF']._serialized_end=223
  _globals['_FIELDDEF_ENUMDEF']._serialized_start=225
  _globals['_FIELDDEF_ENUMDEF']._serialized_end=332
  _globals['_FIELDDEF_ENUMDEF_VALUEENTRY']._serialized_start=288
  _globals['_FIELDDEF_ENUMDEF_VALUEENTRY']._serialized_end=332
  _globals['_FIELDDEF_MESSAGEDEF']._serialized_start=335
  _globals['_FIELDDEF_MESSAGEDEF']._serialized_end=629
  _globals['_FIELDDEF_MESSAGEDEF_PARAMDEF']._serialized_start=457
  _globals['_FIELDDEF_MESSAGEDEF_PARAMDEF']._serialized_end=518
  _globals['_FIELDDEF_MESSAGEDEF_ONEOFDEF']._serialized_start=520
  _globals['_FIELDDEF_MESSAGEDEF_ONEOFDEF']._serialized_end=545
  _globals['_FIELDDEF_MESSAGEDEF_PARAMENTRY']._serialized_start=547
  _globals['_FIELDDEF_MESSAGEDEF_PARAMENTRY']._serialized_end=629
  _globals['_CONTRACTLEDGER']._serialized_start=640
  _globals['_CONTRACTLEDGER']._serialized_end=713
  _globals['_METADATA']._serialized_start=716
  _globals['_METADATA']._serialized_end=1123
  _globals['_METADATA_HASHTAG']._serialized_start=867
  _globals['_METADATA_HASHTAG']._serialized_end=1100
  _globals['_METADATA_HASHTAG_HASH']._serialized_start=996
  _globals['_METADATA_HASHTAG_HASH']._serialized_end=1031
  _globals['_METADATA_HASHTAG_ATTRHASHTAG']._serialized_start=1033
  _globals['_METADATA_HASHTAG_ATTRHASHTAG']._serialized_end=1100
  _globals['_APPDEF']._serialized_start=1126
  _globals['_APPDEF']._serialized_end=1331
  _globals['_APPDEF_METHODDEF']._serialized_start=1180
  _globals['_APPDEF_METHODDEF']._serialized_end=1258
  _globals['_APPDEF_METHODENTRY']._serialized_start=1260
  _globals['_APPDEF_METHODENTRY']._serialized_end=1331
  _globals['_SERVICE']._serialized_start=1334
  _globals['_SERVICE']._serialized_end=2529
  _globals['_SERVICE_API']._serialized_start=1483
  _globals['_SERVICE_API']._serialized_end=1712
  _globals['_SERVICE_API_PROTOCOL']._serialized_start=1581
  _globals['_SERVICE_API_PROTOCOL']._serialized_end=1636
  _globals['_SERVICE_API_SLOT']._serialized_start=1638
  _globals['_SERVICE_API_SLOT']._serialized_end=1712
  _globals['_SERVICE_CONTAINER']._serialized_start=1715
  _globals['_SERVICE_CONTAINER']._serialized_end=2473
  _globals['_SERVICE_CONTAINER_ARCHITECTURE']._serialized_start=1981
  _globals['_SERVICE_CONTAINER_ARCHITECTURE']._serialized_end=2040
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_start=2043
  _globals['_SERVICE_CONTAINER_FILESYSTEM']._serialized_end=2337
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_start=2123
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH']._serialized_end=2337
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK']._serialized_start=2297
  _globals['_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK']._serialized_end=2329
  _globals['_SERVICE_CONTAINER_CONFIG']._serialized_start=2339
  _globals['_SERVICE_CONTAINER_CONFIG']._serialized_end=2395
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_start=2397
  _globals['_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY']._serialized_end=2473
  _globals['_SERVICE_NETWORK']._serialized_start=2475
  _globals['_SERVICE_NETWORK']._serialized_end=2529
  _globals['_INSTANCE']._serialized_start=2532
  _globals['_INSTANCE']._serialized_end=2724
  _globals['_INSTANCE_URI']._serialized_start=2623
  _globals['_INSTANCE_URI']._serialized_end=2654
  _globals['_INSTANCE_URI_SLOT']._serialized_start=2656
  _globals['_INSTANCE_URI_SLOT']._serialized_end=2724
  _globals['_CONFIGURATION']._serialized_start=2727
  _globals['_CONFIGURATION']._serialized_end=2899
  _globals['_CONFIGURATION_ENVIROMENTVARIABLESENTRY']._serialized_start=2841
  _globals['_CONFIGURATION_ENVIROMENTVARIABLESENTRY']._serialized_end=2899
  _globals['_CONFIGURATIONFILE']._serialized_start=2902
  _globals['_CONFIGURATIONFILE']._serialized_end=3047
  _globals['_SYSRESOURCES']._serialized_start=3050
  _globals['_SYSRESOURCES']._serialized_end=3264
# @@protoc_insertion_point(module_scope)
