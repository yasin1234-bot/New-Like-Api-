# gen_pb2.py — একবার চালান, তারপর ডিলিট করে দিন
from google.protobuf import descriptor_pb2

fdp = descriptor_pb2.FileDescriptorProto()
fdp.name = "like_count.proto"
fdp.syntax = "proto3"

# ---- BasicInfo ----
bi = fdp.message_type.add()
bi.name = "BasicInfo"

f = bi.field.add()
f.name = "UID"; f.number = 1
f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
f.type = descriptor_pb2.FieldDescriptorProto.TYPE_INT64
f.json_name = "UID"

f = bi.field.add()
f.name = "PlayerNickname"; f.number = 3
f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
f.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING
f.json_name = "PlayerNickname"

f = bi.field.add()
f.name = "Level"; f.number = 6
f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
f.type = descriptor_pb2.FieldDescriptorProto.TYPE_INT32
f.json_name = "Level"

f = bi.field.add()
f.name = "Likes"; f.number = 21
f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
f.type = descriptor_pb2.FieldDescriptorProto.TYPE_INT64
f.json_name = "Likes"

# ---- Info ----
info = fdp.message_type.add()
info.name = "Info"

f = info.field.add()
f.name = "AccountInfo"; f.number = 1
f.label = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL
f.type = descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
f.type_name = ".BasicInfo"
f.json_name = "AccountInfo"

serialized = fdp.SerializeToString()

# ---- প্রিন্ট করা বাইট ----
print("TOTAL BYTES:", len(serialized))
print("HEX:", serialized.hex())

# ---- like_count_pb2.py জেনারেট ----
hex_bytes = ""
for i in range(0, len(serialized), 16):
    chunk = serialized[i:i+16]
    hex_bytes += "    b'" + "".join(f"\\x{b:02x}" for b in chunk) + "'\n"

code = f'''# -*- coding: utf-8 -*-
"""Auto-generated with Level support"""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
{hex_bytes})

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'like_count_pb2', _globals)
'''

with open("like_count_pb2.py", "w") as fp:
    fp.write(code)

print("✅ like_count_pb2.py generated OK")