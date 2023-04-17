import sys

dest = {'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111', 'null':'000'}
jump = {'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111', 'null':'000'}
comp = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'000111', '-A':'0110011', 'D+1':'0011111', 'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 
'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}
constants = {'R0':'0', 'R1':'1', 'R2':'2', 'R3':'3', 'R4':'4', 'R5':'5', 'R6':'6', 'R7':'7', 'R8':'8', 'R9':'9', 'R10':'10', 'R11':'11', 'R12':'12', 'R13':'13', 'R14':'14', 'R15':'15', 'SCREEN':'16384', 'KBD':'24576', 'SP':'0', 'LCL':'1', 'ARG':'2', 'THIS':'3', 'THAT':'4'}
user_labels = {}
line_num = 0

def parse_input(lines):
    lines_delimed = []
    for line in lines:
        delim = line.find('//')
        if delim != -1:
            while(line[delim-1] == ' '):
                delim -= 1
        else:
            delim = len(line) - 1
            while(line[delim-1] == ' '):
                delim -= 1

        delim_left = line.find(' ')
        if delim_left == 0:
            while(line[delim_left] == ' '):
                delim_left += 1
            lines_delimed.append(line[delim_left:delim])
        else:
            lines_delimed.append(line[:delim])

    return lines_delimed

def parse_label(label):
    global line_num
    if label not in user_labels:
        user_labels[label] = line_num

def construct_jump_table(lines_delimed):
    global line_num
    for line in lines_delimed:
        delim = line.find('(')
        if delim != -1:
            delim_right = line.find(')')
            parse_label(line[delim+1:delim_right])
            continue
        delim = line.find('@')
        if delim != -1:
            line_num += 1
            continue
        delim = line.find('=')
        if delim != -1:
            line_num += 1
            continue
        delim = line.find(';')
        if delim != -1:
            line_num += 1

def construct_user_variables(lines_delimed):
    line_num = 16
    for line in lines_delimed:
        delim = line.find('@')
        if delim != -1:
            if line[delim+1:] not in constants and line[delim+1:] not in user_labels and line[delim+1:].isdigit() == False:
                user_labels[line[delim+1:]] = line_num
                line_num += 1

def translation(lines_delimed):
    with open(sys.argv[2], 'w') as f:
        for line in lines_delimed:
            delim = line.find('@')
            if delim != -1:
                if line[delim+1:].isdigit():
                    f.write('0' + bin(int(line[delim+1:]))[2:].zfill(15))
                elif line[delim+1:] in constants:
                    f.write('0' + bin(int(constants[line[delim+1:]]))[2:].zfill(15))
                else:
                    f.write('0' + bin(int(user_labels[line[delim+1:]]))[2:].zfill(15))
                f.write('\n')
                continue
            delim = line.find('=')
            if delim != -1:
                f.write('111' + comp[line[delim+1:]] + dest[line[:delim]] + jump['null'])
                f.write('\n')
                continue
            delim = line.find(';')
            if delim != -1:
                f.write('111' + comp[line[:delim]] + dest['null'] + jump[line[delim+1:]])
                f.write('\n')

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines_delimed = parse_input(lines)
    construct_jump_table(lines_delimed)
    construct_user_variables(lines_delimed)
    translation(lines_delimed)
    f.close()