buffer_overflow_1:: buffer_overflow_1.c
	gcc -m32 buffer_overflow_1.c -fno-stack-protector -g -o buffer_overflow_1
	objdump -D -M intel buffer_overflow_1 > buffer_overflow_1.diss

buffer_overflow_2:: buffer_overflow_2.c
	gcc -m32 buffer_overflow_2.c -fno-stack-protector -g -o buffer_overflow_2
	objdump -D -M intel buffer_overflow_2 > buffer_overflow_2.diss

shell_exploit_1:: shell_exploit_1.c
	gcc -m32 shell_exploit_1.c -fno-stack-protector -g -z execstack -o shell_exploit_1
	objdump -D -M intel shell_exploit_1 > shell_exploit_1.diss

shell_exploit_2: shell_exploit_2.c
	gcc -m32 shell_exploit_2.c -fno-stack-protector -g -z execstack -o shell_exploit_2
	objdump -D -M intel shell_exploit_2 > shell_exploit_2.diss

shell_asm: shell_asm.asm
	nasm -f elf shell_asm.asm -o shell_asm.o
	ld -m elf_i386 shell_asm.o -o shell_asm
	objdump -D -M intel shell_asm > shell_asm.diss

shell_c: shell_c.c
	gcc -static shell_c.c -o shell_c -m32 -static -fno-stack-protector -g
	objdump -D -M intel shell_c > shell_c.diss

ret_2_libc: ret_2_libc.c
	gcc -static ret_2_libc.c -o ret_2_libc -m32 -static -fno-stack-protector -g
	objdump -D -M intel ret_2_libc > ret_2_libc.diss

skip_instruction: skip_instruction.c
	gcc -static skip_instruction.c -o skip_instruction -m32 -static -fno-stack-protector -g
	objdump -D -M intel skip_instruction > skip_instruction.diss

clean:
	rm shell_exploit_1 -f
	rm shell_exploit_2 -f
	rm buffer_overflow_2 -f
	rm buffer_overflow_1 -f
	rm buffer_overflow_1.diss -f
	rm buffer_overflow_2.diss -f
	rm shell_exploit_1.diss -f
	rm shell_exploit_2.diss -f
	rm shell_asm.diss -f
	rm shell_asm -f
	rm shell_c -f
	rm shell_c.diss -f
	rm shell_asm.o -f
	rm shell.o -f
	rm skip_instruction.diss -f
	rm skip_instruction -f
	rm ret_2_libc -f
	rm ret_2_libc.diss -f