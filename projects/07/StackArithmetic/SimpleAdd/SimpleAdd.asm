// push constant 7
@7
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
@14
M=D
@14
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
