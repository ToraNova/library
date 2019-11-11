; HelloWorld.asm
; Hello World example in assembly x86
;
; ToraNova
; 2019 Oct 27
; based on John Hammond's demo on youtube
; compile with nasm -f elf32 -o helloworld.o <thisfilename>
; then link with ld -m elf_i386 -o helloworld helloworld.o

global _start

;code / program section
section .code:

_start:
	mov eax, 0x4	; setup to call the WRITE syscall
	mov ebx, 0x1	; stdout as file descriptor
	mov ecx, msgstr ; msgstr as buffer
	mov edx, msglen ; msglen as size_t
	int 0x80	; syscall interrupt
	; eax has the return value of the syscall

	mov eax, 0x1 	; setup syscall to gracefully exit program
	mov ebx, 0	; exit code
	int 0x80 	; syscall interrupt

;data / variables section
section .data:
	msgstr: db "Hello World!",0xA
	msglen equ $-msgstr;
