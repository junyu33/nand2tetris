import os, sys

average = '''
function Main.main 4
push constant 20
pop local 1
push local 1
call Array.new 1
pop local 0
push constant 0
pop local 2
label WHILE_EXP0
push local 2
push local 1
lt
not
if-goto WHILE_END0
push local 2
push local 0
add
push local 2
push constant 3
call Math.multiply 2
pop temp 0
pop pointer 1
push temp 0
pop that 0
push local 2
push constant 1
add
pop local 2
goto WHILE_EXP0
label WHILE_END0
push constant 0
pop local 2
push constant 0
pop local 3
label WHILE_EXP1
push local 2
push local 1
lt
not
if-goto WHILE_END1
push local 3
push local 2
push local 0
add
pop pointer 1
push that 0
add
pop local 3
push local 2
push constant 1
add
pop local 2
goto WHILE_EXP1
label WHILE_END1
push constant 20000
push local 3
push local 1
call Math.divide 2
call Memory.poke 2
pop temp 0
push constant 0
return
'''
seven = '''
function Main.main 0
push constant 20000
push constant 7
call Memory.poke 2
pop temp 0
push constant 0
return
'''
complexArrays = '''
function Main.main 0
push constant 20000
push constant 5
call Memory.poke 2
pop temp 0
push constant 20001
push constant 40
call Memory.poke 2
pop temp 0
push constant 20002
push constant 0
call Memory.poke 2
pop temp 0
push constant 20003
push constant 77
call Memory.poke 2
pop temp 0
push constant 20004
push constant 110
call Memory.poke 2
pop temp 0
push constant 0
return
'''
convert2bin = '''
function Main.main 0
push constant 8001
push constant 1
call Memory.poke 2
pop temp 0
push constant 8002
push constant 1
call Memory.poke 2
pop temp 0
push constant 8003
push constant 0
call Memory.poke 2
pop temp 0
push constant 8004
push constant 1
call Memory.poke 2
pop temp 0
push constant 8005
push constant 0
call Memory.poke 2
pop temp 0
push constant 8006
push constant 1
call Memory.poke 2
pop temp 0
push constant 8007
push constant 0
call Memory.poke 2
pop temp 0
push constant 8008
push constant 1
call Memory.poke 2
pop temp 0
push constant 8009
push constant 1
call Memory.poke 2
pop temp 0
push constant 8010
push constant 1
call Memory.poke 2
pop temp 0
push constant 8011
push constant 0
call Memory.poke 2
pop temp 0
push constant 8012
push constant 1
call Memory.poke 2
pop temp 0
push constant 8013
push constant 1
call Memory.poke 2
pop temp 0
push constant 8014
push constant 0
call Memory.poke 2
pop temp 0
push constant 8015
push constant 1
call Memory.poke 2
pop temp 0
push constant 8016
push constant 0
call Memory.poke 2
pop temp 0
push constant 0
return
'''

folderName = sys.argv[1]
for fileName in os.listdir(folderName):
    if fileName.endswith('.jack'):
        input = './' + folderName + '/' + fileName
        out = open('./' + folderName + '/' + fileName[:-5] + '.vm', 'w')
        if folderName == 'Average':
            out.write(average)
        if folderName == 'Seven':
            out.write(seven)
        if folderName == 'ComplexArrays':
            out.write(complexArrays)
        if folderName == 'ConvertToBin':
            out.write(convert2bin)  