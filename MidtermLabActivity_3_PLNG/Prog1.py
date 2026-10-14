
message = "Hello Python"


bytes_msg = message.encode('utf-8')
print(f"Task 1: {bytes_msg}")


string_msg = bytes_msg.decode('utf-8')
print(f"Task 2: {string_msg}")


hex_str = bytes_msg.hex()
print(f"Task 3: {hex_str}")


bytes_from_hex = bytes.fromhex(hex_str)
print(f"Task 4: {bytes_from_hex}")


bytearray_direct = bytearray(message, 'utf-8')
print(f"Task 5: {bytearray_direct}")

bytearray_from_bytes = bytearray(bytes_msg)
print(f"Task 6: {bytearray_from_bytes}")


sliced_bytes = bytes_msg[6:]
print(f"Task 7: {sliced_bytes}")


bytearray_from_bytes[0] = 104 
decoded_modified = bytearray_from_bytes.decode('utf-8')
print(f"Task 8: {decoded_modified}")
