@256
D=A
@0
M=D
@Sys.init20000
D=A
@0
A=M
M=D
@0
D=M
M=D+1
@1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@2
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@3
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@4
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@0
D=M
@5
D=D-A
@0
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Sys.init
0;JMP
(Sys.init20000)
(END)
@END
0;JMP
// function Class2.set 0
(Class2.set)
// push argument 0
@0
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@14
A=M
D=M
@13
A=M
M=D
@0
D=M
M=D+1
// pop static 0
@0
D=M
M=D-1
@0
D=M
@13
M=D
@13
A=M
D=M
@Class2.0
M=D
// push argument 1
@0
D=M
@13
M=D
@2
D=M
@1
D=D+A
@14
M=D
@14
A=M
D=M
@13
A=M
M=D
@0
D=M
M=D+1
// pop static 1
@0
D=M
M=D-1
@0
D=M
@13
M=D
@13
A=M
D=M
@Class2.1
M=D
// push constant 0
@0
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// return
@1
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@2
A=M
M=D
@2
D=M
@0
M=D+1
@endFrame
D=M
@1
A=D-A
D=M
@4
M=D
@endFrame
D=M
@2
A=D-A
D=M
@3
M=D
@endFrame
D=M
@3
A=D-A
D=M
@2
M=D
@endFrame
D=M
@4
A=D-A
D=M
@1
M=D
@retAddr
A=M
0;JMP
// function Class2.get 0
(Class2.get)
// push static 0
@Class2.0
D=M
@0
A=M
M=D
@0
D=M
M=D+1
// push static 1
@Class2.1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
// sub
@0
D=M
M=D-1
@0
A=M
D=M
@13
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@13
A=M
D=D - A
@0
A=M
M=D
@0
D=M
M=D+1
// return
@1
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@2
A=M
M=D
@2
D=M
@0
M=D+1
@endFrame
D=M
@1
A=D-A
D=M
@4
M=D
@endFrame
D=M
@2
A=D-A
D=M
@3
M=D
@endFrame
D=M
@3
A=D-A
D=M
@2
M=D
@endFrame
D=M
@4
A=D-A
D=M
@1
M=D
@retAddr
A=M
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 6
@6
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// push constant 8
@8
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// call Class1.set 2
@Class1.set20001
D=A
@0
A=M
M=D
@0
D=M
M=D+1
@1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@2
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@3
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@4
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@0
D=M
@5
D=D-A
@2
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Class1.set
0;JMP
(Class1.set20001)
// pop temp 0 // Dumps the return value
@0
D=M
M=D-1
@0
D=M
@13
M=D
@5
D=A
@0
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// push constant 23
@23
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// push constant 15
@15
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// call Class2.set 2
@Class2.set20002
D=A
@0
A=M
M=D
@0
D=M
M=D+1
@1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@2
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@3
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@4
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@0
D=M
@5
D=D-A
@2
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Class2.set
0;JMP
(Class2.set20002)
// pop temp 0 // Dumps the return value
@0
D=M
M=D-1
@0
D=M
@13
M=D
@5
D=A
@0
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// call Class1.get 0
@Class1.get20003
D=A
@0
A=M
M=D
@0
D=M
M=D+1
@1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@2
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@3
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@4
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@0
D=M
@5
D=D-A
@0
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Class1.get
0;JMP
(Class1.get20003)
// call Class2.get 0
@Class2.get20004
D=A
@0
A=M
M=D
@0
D=M
M=D+1
@1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@2
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@3
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@4
D=M
@0
A=M
M=D
@0
D=M
M=D+1
@0
D=M
@5
D=D-A
@0
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Class2.get
0;JMP
(Class2.get20004)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0;JMP
// function Class1.set 0
(Class1.set)
// push argument 0
@0
D=M
@13
M=D
@2
D=M
@0
D=D+A
@14
M=D
@14
A=M
D=M
@13
A=M
M=D
@0
D=M
M=D+1
// pop static 0
@0
D=M
M=D-1
@0
D=M
@13
M=D
@13
A=M
D=M
@Class1.0
M=D
// push argument 1
@0
D=M
@13
M=D
@2
D=M
@1
D=D+A
@14
M=D
@14
A=M
D=M
@13
A=M
M=D
@0
D=M
M=D+1
// pop static 1
@0
D=M
M=D-1
@0
D=M
@13
M=D
@13
A=M
D=M
@Class1.1
M=D
// push constant 0
@0
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// return
@1
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@2
A=M
M=D
@2
D=M
@0
M=D+1
@endFrame
D=M
@1
A=D-A
D=M
@4
M=D
@endFrame
D=M
@2
A=D-A
D=M
@3
M=D
@endFrame
D=M
@3
A=D-A
D=M
@2
M=D
@endFrame
D=M
@4
A=D-A
D=M
@1
M=D
@retAddr
A=M
0;JMP
// function Class1.get 0
(Class1.get)
// push static 0
@Class1.0
D=M
@0
A=M
M=D
@0
D=M
M=D+1
// push static 1
@Class1.1
D=M
@0
A=M
M=D
@0
D=M
M=D+1
// sub
@0
D=M
M=D-1
@0
A=M
D=M
@13
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@13
A=M
D=D - A
@0
A=M
M=D
@0
D=M
M=D+1
// return
@1
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@0
D=M
M=D-1
@0
A=M
D=M
@2
A=M
M=D
@2
D=M
@0
M=D+1
@endFrame
D=M
@1
A=D-A
D=M
@4
M=D
@endFrame
D=M
@2
A=D-A
D=M
@3
M=D
@endFrame
D=M
@3
A=D-A
D=M
@2
M=D
@endFrame
D=M
@4
A=D-A
D=M
@1
M=D
@retAddr
A=M
0;JMP
