buffer_overflow_1: buffer_overflow_1.c
	gcc -m32 buffer_overflow_1.c -fno-stack-protector -g -o buffer_overflow_1
	objdump -D -M intel buffer_overflow_1 > buffer_overflow_1.diss

buffer_overflow_2: buffer_overflow_2.c
	gcc -m32 buffer_overflow_2.c -fno-stack-protector -g -o buffer_overflow_2
	objdump -D -M intel buffer_overflow_2 > buffer_overflow_2.diss

shell_exploit_1:
	gcc -m32 shell_exploit_1.c -fno-stack-protector -g -z execstack -o shell_exploit_1
	objdump -D -M intel shell_exploit_1 > shell_exploit_1.diss

shell_exploit_2:
	gcc -m32 shell_exploit_2.c -fno-stack-protector -g -z execstack -o shell_exploit_2
	objdump -D -M intel shell_exploit_2 > shell_exploit_2.diss

shell_asm:
	nasm -f elf shell_asm.asm -o shell_asm.o
	ld -m elf_i386 shell_asm.o -o shell_asm
	objdump -D -M intel shell_asm > shell_asm.diss

shell_c:
	gcc -static shell_c.c -o shell_c -m32 -static -fno-stack-protector -g
	objdump -D -M intel shell_c > shell_c.diss

skip_instruction:
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