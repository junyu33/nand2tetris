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
// function Sys.init 0
(Sys.init)
// push constant 4000	// test THIS and THAT context save
@4000	//
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 0
@0
D=M
M=D-1
@0
A=M
D=M
@3
M=D
// push constant 5000
@5000
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 1
@0
D=M
M=D-1
@0
A=M
D=M
@4
M=D
// call Sys.main 0
@Sys.main20001
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
@Sys.main
0;JMP
(Sys.main20001)
// pop temp 1
@0
D=M
M=D-1
@0
D=M
@13
M=D
@5
D=A
@1
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// label LOOP
(LOOP)
// goto LOOP
@LOOP
0;JMP
// function Sys.main 5
(Sys.main)
@0
A=M
M=0
@0
D=M
M=D+1
@0
A=M
M=0
@0
D=M
M=D+1
@0
A=M
M=0
@0
D=M
M=D+1
@0
A=M
M=0
@0
D=M
M=D+1
@0
A=M
M=0
@0
D=M
M=D+1
// push constant 4001
@4001
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 0
@0
D=M
M=D-1
@0
A=M
D=M
@3
M=D
// push constant 5001
@5001
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 1
@0
D=M
M=D-1
@0
A=M
D=M
@4
M=D
// push constant 200
@200
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop local 1
@0
D=M
M=D-1
@0
D=M
@13
M=D
@1
D=M
@1
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// push constant 40
@40
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop local 2
@0
D=M
M=D-1
@0
D=M
@13
M=D
@1
D=M
@2
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// push constant 6
@6
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop local 3
@0
D=M
M=D-1
@0
D=M
@13
M=D
@1
D=M
@3
D=D+A
@14
M=D
@13
A=M
D=M
@14
A=M
M=D
// push constant 123
@123
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// call Sys.add12 1
@Sys.add1220002
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
@1
D=D-A
@2
M=D
@0
D=M
@1
M=D
@Sys.add12
0;JMP
(Sys.add1220002)
// pop temp 0
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
// push local 0
@0
D=M
@13
M=D
@1
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
// push local 1
@0
D=M
@13
M=D
@1
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
// push local 2
@0
D=M
@13
M=D
@1
D=M
@2
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
// push local 3
@0
D=M
@13
M=D
@1
D=M
@3
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
// push local 4
@0
D=M
@13
M=D
@1
D=M
@4
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
// add
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
D=D + A
@0
A=M
M=D
@0
D=M
M=D+1
// add
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
D=D + A
@0
A=M
M=D
@0
D=M
M=D+1
// add
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
D=D + A
@0
A=M
M=D
@0
D=M
M=D+1
// add
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
D=D + A
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
// function Sys.add12 0
(Sys.add12)
// push constant 4002
@4002
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 0
@0
D=M
M=D-1
@0
A=M
D=M
@3
M=D
// push constant 5002
@5002
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// pop pointer 1
@0
D=M
M=D-1
@0
A=M
D=M
@4
M=D
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
// push constant 12
@12
D=A
@0
A=M
M=D
@0
D=M
M=D+1
// add
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
D=D + A
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
