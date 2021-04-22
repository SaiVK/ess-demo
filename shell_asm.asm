section .text
global _start
_start:
; Goal: execve("/bin//sh", [&("/bin//sh"), 0], 0)
; Note that:
xor    eax,eax          ; Step 1: Load string "/bin//sh\0" on stack.
push   eax              ; "\0"
push   0x68732f2f       ; "//sh"
push   0x6e69622f       ; "/bin"
mov    ebx,esp          ; Step 2: Load ebx with address where "/bin//sh\0" is stored
push   eax              ; Step 3: Load array [&("/bin//sh"), 0]
push   ebx              ;   
mov    ecx,esp          ; Step 4: Load ecx with address where array [&("/bin//sh"), 0] is stored
mov    al,0xb           ; Step 5: Set eax -> 11 (execve system call number w.r.t x86 32 bit System ABI )
int    0x80             ; Trap to kernel to execute system call