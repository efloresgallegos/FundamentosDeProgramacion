; hola.asm - Hola mundo en x86-64 Linux con syscalls
; Ensamblador: NASM

        global  _start

        section .data
msg:    db      "Hola, mundo!", 10      ; 10 = '\n'
len:    equ     $ - msg

        section .text
_start:
        ; write(1, msg, len)
        mov     rax, 1          ; syscall: write
        mov     rdi, 1          ; fd: stdout
        mov     rsi, msg        ; buffer
        mov     rdx, len        ; tamaño
        syscall

        ; exit(0)
        mov     rax, 60         ; syscall: exit
        xor     rdi, rdi        ; código 0
        syscall