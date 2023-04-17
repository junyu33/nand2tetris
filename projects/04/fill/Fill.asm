// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// (LOOP)
// tmp = *keyboard
// if (tmp > 0) {
//     while (true) {
//         ptr = &screen;
//         *ptr = -1;
//         ptr += 1;
//         if (ptr == keyboard) goto LOOP;
//     }
// } else {
//     while (true) {
//         ptr = &screen;
//         *ptr = 0;
//         ptr += 1;
//         if (ptr == keyboard) goto LOOP;
//     }
// }

(LOOP)
    @LOOP
    @KBD
    D=M 
    @tmp
    M=D // tmp = *keyboard
    @KBD
    D=A 
    @keyboard
    M=D // keyboard = &keyboard
    @tmp
    D=M
    @PRE
    D; JEQ // if (tmp == 0) goto WHITE

    @SCREEN
    D=A
    @ptr
    M=D // ptr = &screen
(BLACK)
    A=D
    M=-1 // *ptr = -1

    @ptr
    M=M+1
    D=M // ptr = ptr + 1
    
    @KBD
    D=D-A // D = ptr - keyboard
    @LOOP
    D; JEQ // if (ptr - keyboard == 0) goto LOOP;
    @KBD
    D=D+A
    @BLACK
    0; JMP // else goto BLACK

(PRE)
    @SCREEN
    D=A
    @ptr
    M=D // ptr = &screen
(WHITE)
    A=D
    M=0 // *ptr = 0

    @ptr
    M=M+1
    D=M // ptr = ptr + 1
    
    @KBD
    D=D-A // D = ptr - keyboard
    @LOOP
    D; JEQ // if (ptr - keyboard == 0) goto LOOP;
    @KBD
    D=D+A
    @WHITE
    0; JMP // else goto WHITE
