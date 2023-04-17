import sys, os

segdict = {
    'local': '1',
    'argument': '2',
    'this': '3',
    'that': '4',
}

thisthat = {
    '0' : '3',
    '1' : '4',
}

condCount = 10000
callCount = 20000
methodName = ''

def parsePop(seg, val):
    if seg in ['local', 'argument', 'this', 'that']: # addr = LCL + val; SP--; *addr = *SP
        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D-1', file=out) # SP = SP-1

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('@13', file=out)
        print('M=D', file=out) # *R13 = SP

        print('@' + segdict[seg], file=out)
        print('D=M', file=out) # D=*seg
        print('@' + val, file=out)
        print('D=D+A', file=out) # D=*seg + val
        print('@14', file=out)
        print('M=D', file=out) # *R14 = D

        print('@13', file=out)
        print('A=M', file=out) # A = SP
        print('D=M', file=out) # D = *SP
        print('@14', file=out)
        print('A=M', file=out) # A=*R14
        print('M=D', file=out) # *A = D

    if seg == 'static': 
        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D-1', file=out) # SP = SP-1

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('@13', file=out)
        print('M=D', file=out) # *R13 = SP
    
        print('@13', file=out)
        print('A=M', file=out) # A = SP
        print('D=M', file=out) # D = *SP
        print('@' + methodName.split('.')[0] + '.' + val, file=out)
        print('M=D', file=out)

    if seg == 'temp': # addr = 5 + val; SP--; *addr = *SP
        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D-1', file=out) # SP = SP-1

        print('@0', file=out)
        print('D=M', file=out) # D=*SP
        print('@13', file=out)
        print('M=D', file=out) # *R13 = D

        print('@5', file=out)
        print('D=A', file=out) # D=5
        print('@' + val, file=out)
        print('D=D+A', file=out) # D=5 + val
        print('@14', file=out)
        print('M=D', file=out) # *R14 = D

        print('@13', file=out)
        print('A=M', file=out) # A = SP
        print('D=M', file=out) # D = *SP
        print('@14', file=out)
        print('A=M', file=out) # A=*R14
        print('M=D', file=out) # *A = D
    
    if seg == 'pointer': # SP--; THIS/THAT = *SP
        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D-1', file=out) # SP = SP-1

        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('D=M', file=out) # D=*SP

        print('@' + thisthat[val], file=out)
        print('M=D', file=out) # *THIS/THAT = D



def parsePush(seg, val):
    if seg in ['local', 'argument', 'this', 'that']: # addr = *seg + val; *SP = *addr;  SP++;
        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('@13', file=out)
        print('M=D', file=out) # *R13 = SP

        print('@' + segdict[seg], file=out)
        print('D=M', file=out) # D=*seg
        print('@' + val, file=out)
        print('D=D+A', file=out) # D=*seg + val
        print('@14', file=out)
        print('M=D', file=out) # *R14 = D

        print('@14', file=out)
        print('A=M', file=out) # D=*seg + val
        print('D=M', file=out) # D=*addr
        print('@13', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = *addr

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

    if seg == 'constant': # *SP = val; SP++;
        print('@' + val, file=out)
        print('D=A', file=out) # D=val
        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = D

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

    if seg == 'static': 
        print('@' + methodName.split('.')[0] + '.' + val, file=out)
        print('D=M', file=out)
        
        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = D

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

    if seg == 'temp': # addr = 5 + val; *SP = *addr; SP++;
        print('@0', file=out)
        print('D=M', file=out) # D=*SP
        print('@13', file=out)
        print('M=D', file=out) # *R13 = SP

        print('@5', file=out)
        print('D=A', file=out) # D=5
        print('@' + val, file=out)
        print('D=D+A', file=out) # D=5 + val
        print('@14', file=out)
        print('M=D', file=out) # *R14 = D

        print('@14', file=out)
        print('A=M', file=out) # D=*seg + val
        print('D=M', file=out) # D=*addr
        print('@13', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = *addr

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

    if seg == 'pointer': # *SP = THIS/THAT; SP++;
        print('@' + thisthat[val], file=out)
        print('D=M', file=out) # D=*THIS/THAT

        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = D

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1


def parseTwo(op): # SP--; SP--; *SP = *SP + *SP; SP++;
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    print('@13', file=out)
    print('M=D', file=out) # *R13 = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    # print('@14', file=out)
    # print('M=D', file=out) # *R14 = D

    # print('@14', file=out)
    # print('D=M', file=out) # D=*R14
    print('@13', file=out)
    print('A=M', file=out) # A=*R13
    print('D=D', op, 'A', file=out) # D=D+A
    
    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('M=D', file=out) # *SP = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D+1', file=out) # SP = SP+1


def parseOne(op): # SP--; *SP = -*SP; SP++;
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    # print('@13', file=out)
    # print('M=D', file=out) # *R13 = D

    # print('@13', file=out)
    # print('D=M', file=out) # D=*R13
    print('D=', op, 'D', file=out) # D=-D

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('M=D', file=out) # *SP = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D+1', file=out) # SP = SP+1

def parseCond(cond): # SP--; SP--; *SP = *SP == *SP; SP++;
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    print('@13', file=out)
    print('M=D', file=out) # *R13 = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    # print('@14', file=out)
    # print('M=D', file=out) # *R14 = D
    
    # print('@14', file=out)
    # print('D=M', file=out) # D=*R14
    print('@13', file=out)
    print('A=M', file=out) # A=*R13
    print('D=D-A', file=out) # D=*R14 - *R13

    global condCount
    print('@' + cond + str(condCount), file=out)
    print('D;', cond, file=out) # if D == 0 goto condCount
    print('@0', file=out)
    print('D=0', file=out) # D=0
    print('@' + cond + str(condCount) + 'end', file=out)
    print('0;JMP', file=out) # goto condCount + 'end'
    print('(' + cond + str(condCount) + ')', file=out)
    print('@0', file=out)
    print('D=-1', file=out) # D=-1
    print('(' + cond + str(condCount) + 'end)', file=out)
    condCount += 1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('M=D', file=out) # *SP = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D+1', file=out) # SP = SP+1

def parseLabel(label):
    print('(' + label + ')', file=out)

def parseGoto(label):
    print('@' + label, file=out)
    print('0;JMP', file=out)

def parseIf(label):
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP
    print('@' + label, file=out)
    print('M=D', file=out) # *R13 = D
    
    print('@' + label, file=out)
    print('M;', 'JNE', file=out) # if D != 0 goto label

def parseFunction(func, n):
    print('(' + func + ')', file=out)
    for i in range(int(n)):
        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('M=0', file=out) # *SP = 0

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

def parseCall(func, n):
    global callCount
    retAddr = func + str(callCount)
    # push retAddr
    print('@' + retAddr, file=out)
    print('D=A', file=out) # D=retAddr

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('M=D', file=out) # *SP = D

    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D+1', file=out) # SP = SP+1

    # push LCL, ARG, THIS, THAT
    for i in range(4):
        print('@' + str(i + 1), file=out)
        print('D=M', file=out)
        
        print('@0', file=out)
        print('A=M', file=out) # A=SP
        print('M=D', file=out) # *SP = D

        print('@0', file=out)
        print('D=M', file=out) # D=SP
        print('M=D+1', file=out) # SP = SP+1

    # ARG = SP - 5 - n
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('@5', file=out)
    print('D=D-A', file=out) # D=SP-5
    print('@' + n, file=out)
    print('D=D-A', file=out) # D=SP-5-n
    print('@2', file=out)
    print('M=D', file=out) # ARG = D

    # LCL = SP
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('@1', file=out)
    print('M=D', file=out) # LCL = D

    # goto func
    print('@' + func, file=out)
    print('0;JMP', file=out)

    # (retAddr)
    print('(' + retAddr + ')', file=out)

    callCount += 1
    
    

def parseReturn():
    # endFrame = LCL
    print('@1', file=out)
    print('D=M', file=out) # D=LCL
    print('@endFrame', file=out)
    print('M=D', file=out) # endFrame = D

    # retAddr = *(endFrame - 5)
    print('@endFrame', file=out)
    print('D=M', file=out) # D=endFrame
    print('@5', file=out)
    print('A=D-A', file=out) # A=endFrame-5
    print('D=M', file=out) # D=*(endFrame-5)
    print('@retAddr', file=out)
    print('M=D', file=out) # retAddr = D

    # *ARG = pop()
    print('@0', file=out)
    print('D=M', file=out) # D=SP
    print('M=D-1', file=out) # SP = SP-1

    print('@0', file=out)
    print('A=M', file=out) # A=SP
    print('D=M', file=out) # D=*SP

    print('@2', file=out)
    print('A=M', file=out) # A=ARG
    print('M=D', file=out) # *ARG = D

    # SP = ARG + 1
    print('@2', file=out)
    print('D=M', file=out) # D=ARG
    print('@0', file=out)
    print('M=D+1', file=out) # SP = ARG+1

    # THAT = *(endFrame - 1)
    print('@endFrame', file=out)
    print('D=M', file=out) # D=endFrame
    print('@1', file=out)
    print('A=D-A', file=out) # A=endFrame-1
    print('D=M', file=out) # D=*(endFrame-1)
    print('@4', file=out)
    print('M=D', file=out) # LCL = D

    # THIS = *(endFrame - 2)
    print('@endFrame', file=out)
    print('D=M', file=out) # D=endFrame
    print('@2', file=out)
    print('A=D-A', file=out) # A=endFrame-2
    print('D=M', file=out) # D=*(endFrame-2)
    print('@3', file=out)
    print('M=D', file=out) # THIS = D

    # ARG = *(endFrame - 3)
    print('@endFrame', file=out)
    print('D=M', file=out) # D=endFrame
    print('@3', file=out)
    print('A=D-A', file=out) # A=endFrame-3
    print('D=M', file=out) # D=*(endFrame-3)
    print('@2', file=out)
    print('M=D', file=out) # ARG = D

    # LCL = *(endFrame - 4)
    print('@endFrame', file=out)
    print('D=M', file=out) # D=endFrame
    print('@4', file=out)
    print('A=D-A', file=out) # A=endFrame-4
    print('D=M', file=out) # D=*(endFrame-4)
    print('@1', file=out)
    print('M=D', file=out) # LCL = D

    # goto retAddr
    print('@retAddr', file=out)
    print('A=M', file=out) # A=retAddr
    print('0;JMP', file=out)
    

def parse(line):
    if line.startswith('push'):
        seg = line.split(' ')[1]
        val = line.split(' ')[2]
        parsePush(seg, val)
    elif line.startswith('pop'):
        seg = line.split(' ')[1]
        val = line.split(' ')[2]
        parsePop(seg, val)
    elif line.startswith('label'):
        parseLabel(line.split(' ')[1])
    elif line.startswith('goto'):
        parseGoto(line.split(' ')[1])
    elif line.startswith('if-goto'):
        parseIf(line.split(' ')[1])
    elif line.startswith('function'):
        parseFunction(line.split(' ')[1], line.split(' ')[2])
    elif line.startswith('call'):
        parseCall(line.split(' ')[1], line.split(' ')[2])

    elif line.startswith('return'):
        parseReturn()
    elif line.startswith('add'):
        parseTwo('+')
    elif line.startswith('sub'):
        parseTwo('-')
    elif line.startswith('neg'):
        parseOne('-')
    elif line.startswith('eq'):
        parseCond('JEQ')
    elif line.startswith('gt'):
        parseCond('JGT')
    elif line.startswith('lt'):
        parseCond('JLT')
    elif line.startswith('and'):
        parseTwo('&')
    elif line.startswith('or'):
        parseTwo('|')
    elif line.startswith('not'):
        parseOne('!')
    else:
        print('Error: ' + line, file=out)

def decode(lines):
    for line in lines:
        line = line.strip()
        if line.startswith('//') or line == '':
            continue
        print('// ' + line, file=out)
        parse(line)

def bootstrapCode():
    print('@256', file=out)
    print('D=A', file=out)
    print('@0', file=out)
    print('M=D', file=out)
    
    parseCall('Sys.init', '0')

    print('(END)', file=out)
    print('@END', file=out)
    print('0;JMP', file=out)

if __name__ == '__main__':
    fileName = sys.argv[1]
    if 'vm' in fileName:
        imageName = os.path.basename(fileName)
        output = imageName.split('.')[0] + '.asm'
        out = open(fileName[:-3] + '.asm', 'w')
        with open(fileName) as f:
            lines = f.readlines()
            decode(lines)
    else:
        imageName = fileName
        outputPath = './' + imageName + '/' + imageName + '.asm'
        print(outputPath)
        out = open(outputPath, 'w')
        bootstrapCode()
        for file in os.listdir('./' + imageName):
            if file.endswith('.vm'):
                methodName = file.split('.')[0]
                with open('./' + imageName + '/' + file) as f:
                    lines = f.readlines()
                    decode(lines)
