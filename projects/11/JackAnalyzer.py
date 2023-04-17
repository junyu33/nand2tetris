import sys, os

keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '"']

def myWrite(string, indent):
    # replace '<' and '>' with '&lt;' and '&gt;'
    string = string.replace(' < ', ' &lt; ').replace(' > ', ' &gt; ').replace(' & ', ' &amp; ')
    print(' ' * indent + string, file=out)

def debug(idx):
    print('idx = ' + str(idx) + ', token = ' + tokens[idx])

# extract keywords, symbols, identifiers, integers, strings
def tokenize(input):
    tokens = []
    with open(input, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('//') or line.startswith('/*') or line.startswith('*') or line.startswith('*/') or line == '':
                continue
            else:
                for symbol in symbols:
                    line = line.replace(symbol, ' ' + symbol + ' ')
                for i in range(len(line.split())):
                    if line.split()[i] == '/' and line.split()[i + 1] == '/':
                        break
                    tokens.append(line.split()[i])

    return tokens

# tackle strings
def handleStrings(tokens):
    for i in range(len(tokens)):
        if tokens[i] == '"':
            j = i + 1
            while tokens[j] != '"':
                j = j + 1
            tokens[i] = '"' + ' '.join(tokens[i + 1:j]) + '"'
            for k in range(i + 1, j + 1):
                tokens[k] = ''
    return [token for token in tokens if token != '']

# TODO: handle comments
def parseExpressionList(tokens, idx, indent):
    # <expressionList> = (<expression> (',' <expression>)*)?
    myWrite('<expressionList>', indent)
    if tokens[idx] != ')':
        idx = parseExpression(tokens, idx, indent + 2)
        while tokens[idx] == ',':
            myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
            idx = parseExpression(tokens, idx + 1, indent + 2)
    myWrite('</expressionList>', indent)
    return idx

def parseSubroutineCall(tokens, idx, indent):
    # <subroutineCall> = <subroutineName> '(' <expressionList> ')' | (<className> | <varName>) '.' <subroutineName> '(' <expressionList> ')'
    if tokens[idx + 1] == '(':
        idx = parseSubroutineName(tokens, idx, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseExpressionList(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1
    else:
        idx = parseClassName(tokens, idx, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseSubroutineName(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseExpressionList(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1
    return idx

def parseTerm(tokens, idx, indent):
    # <term> = <integerConstant> | <stringConstant> | <keywordConstant> | <varName> | <varName> '[' <expression> ']' | <subroutineCall> | '(' <expression> ')' | '-' <term> | '~' <term>
    myWrite('<term>', indent)
    if tokens[idx] in ['-', '~']:
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseTerm(tokens, idx + 1, indent + 2)
    elif tokens[idx] in ['true', 'false', 'null', 'this']:
        myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
        idx = idx + 1
    elif tokens[idx] == '(':
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseExpression(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1
    elif tokens[idx] in ['int', 'char', 'boolean']:
        idx = parseType(tokens, idx, indent + 2)
    elif tokens[idx] in keywords:
        myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
        idx = idx + 1
    elif tokens[idx] in symbols:
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1
    elif tokens[idx].isdigit():
        myWrite('<integerConstant> ' + tokens[idx] + ' </integerConstant>', indent + 2)
        idx = idx + 1
    elif tokens[idx][0] == '"':
        myWrite('<stringConstant> ' + tokens[idx][1:-1] + ' </stringConstant>', indent + 2)
        idx = idx + 1
    elif tokens[idx + 1] == '[':
        idx = parseVarName(tokens, idx, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseExpression(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1
    elif tokens[idx + 1] in ['(', '.']:
        idx = parseSubroutineCall(tokens, idx, indent)
    else:
        idx = parseVarName(tokens, idx, indent + 2)

    myWrite('</term>', indent)
    return idx


def parseExpression(tokens, idx, indent):
    # <expression> = <term> (<op> <term>)*
    myWrite('<expression>', indent)
    idx = parseTerm(tokens, idx, indent + 2)
    while tokens[idx] in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseTerm(tokens, idx + 1, indent + 2)
    myWrite('</expression>', indent)
    return idx

def parseLetStatement(tokens, idx, indent):
    # <letStatement> = 'let' <varName> ('[' <expression> ']')? '=' <expression> ';'
    myWrite('<letStatement>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = parseVarName(tokens, idx + 1, indent + 2)

    if tokens[idx] == '[':
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseExpression(tokens, idx + 1, indent + 2)
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = idx + 1

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = parseExpression(tokens, idx + 1, indent + 2)

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</letStatement>', indent)
    return idx + 1

def parseIfStatement(tokens, idx, indent):
    # <ifStatement> = 'if' '(' <expression> ')' '{' <statements> '}' ('else' '{' <statements> '}')?
    myWrite('<ifStatement>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    myWrite('<symbol> ' + tokens[idx + 1] + ' </symbol>', indent + 2)
    idx = parseExpression(tokens, idx + 2, indent + 2)

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('<symbol> ' + tokens[idx + 1] + ' </symbol>', indent + 2)
    idx = parseStatements(tokens, idx + 2, indent + 2)

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = idx + 1

    if tokens[idx] == 'else':
        idx = parseElseStatement(tokens, idx, indent)

    myWrite('</ifStatement>', indent)
    return idx

def parseElseStatement(tokens, idx, indent):
    # <elseStatement> = 'else' '{' <statements> '}'
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    myWrite('<symbol> ' + tokens[idx + 1] + ' </symbol>', indent + 2)
    idx = parseStatements(tokens, idx + 2, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    return idx + 1

def parseWhileStatement(tokens, idx, indent):
    # <whileStatement> = 'while' '(' <expression> ')' '{' <statements> '}'
    myWrite('<whileStatement>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    myWrite('<symbol> ' + tokens[idx + 1] + ' </symbol>', indent + 2)
    idx = parseExpression(tokens, idx + 2, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('<symbol> ' + tokens[idx + 1] + ' </symbol>', indent + 2)
    idx = parseStatements(tokens, idx + 2, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</whileStatement>', indent)
    return idx + 1

def parseDoStatement(tokens, idx, indent):
    # <doStatement> = 'do' <subroutineCall> ';'
    myWrite('<doStatement>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = parseSubroutineCall(tokens, idx + 1, indent)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</doStatement>', indent)
    return idx + 1

def parseReturnStatement(tokens, idx, indent):
    # <returnStatement> = 'return' <expression>? ';'
    myWrite('<returnStatement>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = idx + 1
    if tokens[idx] != ';':
        idx = parseExpression(tokens, idx, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</returnStatement>', indent)
    return idx + 1


def parseStatement(tokens, idx, indent):
    # <statement> = <letStatement> | <ifStatement> | <whileStatement> | <doStatement> | <returnStatement>
    if tokens[idx] == 'let':
        idx = parseLetStatement(tokens, idx, indent)
    elif tokens[idx] == 'if':
        idx = parseIfStatement(tokens, idx, indent)
    elif tokens[idx] == 'while':
        idx = parseWhileStatement(tokens, idx, indent)
    elif tokens[idx] == 'do':
        idx = parseDoStatement(tokens, idx, indent)
    elif tokens[idx] == 'return':
        idx = parseReturnStatement(tokens, idx, indent)
    return idx

def parseStatements(tokens, idx, indent):
    # <statements> = <statement>*
    myWrite('<statements>', indent)
    while tokens[idx] in ['let', 'if', 'while', 'do', 'return']:
        idx = parseStatement(tokens, idx, indent + 2)

    myWrite('</statements>', indent)
    return idx

def parseClassName(tokens, idx, indent):
    # <className> = <identifier>
    myWrite('<identifier> ' + tokens[idx] + ' </identifier>', indent)
    return idx + 1

def parseSubroutineName(tokens, idx, indent):
    # <subroutineName> = <identifier>
    myWrite('<identifier> ' + tokens[idx] + ' </identifier>', indent)
    return idx + 1

def parseVarName(tokens, idx, indent):
    # <varName> = <identifier>
    myWrite('<identifier> ' + tokens[idx] + ' </identifier>', indent)
    return idx + 1

def parseVarDec(tokens, idx, indent):
    # <varDec> = 'var' <type> <varName> (',' <varName>)* ';'
    myWrite('<varDec>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = idx + 1

    idx = parseType(tokens, idx, indent + 2)
    idx = parseVarName(tokens, idx, indent + 2)
    while tokens[idx] == ',':
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseVarName(tokens, idx + 1, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</varDec>', indent)
    return idx + 1

def parseSubRoutineBody(tokens, idx, indent):
    # <subroutineBody> = '{' <varDec>* <statements> '}'
    myWrite('<subroutineBody>', indent)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = idx + 1
    while tokens[idx] == 'var':
        idx = parseVarDec(tokens, idx, indent + 2)
    idx = parseStatements(tokens, idx, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</subroutineBody>', indent)
    return idx + 1

def parseParameterList(tokens, idx, indent):
    # <parameterList> = (<type> <varName> (',' <type> <varName>)*)?
    myWrite('<parameterList>', indent)
    if tokens[idx] != ')':
        idx = parseType(tokens, idx, indent + 2)
        idx = parseVarName(tokens, idx, indent + 2)
        while tokens[idx] == ',':
            myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
            idx = idx + 1
            idx = parseType(tokens, idx, indent + 2)
            idx = parseVarName(tokens, idx, indent + 2)

    myWrite('</parameterList>', indent)
    return idx

def parseSubroutineDec(tokens, idx, indent):
    # <subroutineDec> = ('constructor' | 'function' | 'method') ('void' | <type>) <subroutineName> '(' <parameterList> ')' <subroutineBody>
    myWrite('<subroutineDec>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = idx + 1
    if tokens[idx] == 'void':
        myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
        idx = idx + 1
    else:
        idx = parseType(tokens, idx, indent + 2)
    idx = parseSubroutineName(tokens, idx, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = parseParameterList(tokens, idx + 1, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = parseSubRoutineBody(tokens, idx + 1, indent + 2)
    myWrite('</subroutineDec>', indent)
    return idx

def parseType(tokens, idx, indent):
    # <type> = 'int' | 'char' | 'boolean' | <className>
    if tokens[idx] in ['int', 'char', 'boolean']:
        myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent)
    else:
        myWrite('<identifier> ' + tokens[idx] + ' </identifier>', indent)
    return idx + 1

def parseClassVarDec(tokens, idx, indent):
    # <classVarDec> = ('static' | 'field') <type> <varName> (',' <varName>)* ';'
    if tokens[idx] not in ['static', 'field']:
        return idx
    myWrite('<classVarDec>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = idx + 1

    idx = parseType(tokens, idx, indent + 2)
    idx = parseVarName(tokens, idx, indent + 2)

    while tokens[idx] == ',':
        myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
        idx = parseVarName(tokens, idx + 1, indent + 2)

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</classVarDec>', indent)
    return idx + 1

# tokens: tokenize(input)
# idx: index
# indent: indent
def parseClass(tokens, idx, indent):
    # <class> = 'class' <className> '{' <classVarDec>* <subroutineDec>* '}'
    myWrite('<class>', indent)
    myWrite('<keyword> ' + tokens[idx] + ' </keyword>', indent + 2)
    idx = parseClassName(tokens, idx + 1, indent + 2)
    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    idx = idx + 1

    while tokens[idx] in ['static', 'field']:
        idx = parseClassVarDec(tokens, idx, indent + 2)

    while tokens[idx] in ['constructor', 'function', 'method']:
        idx = parseSubroutineDec(tokens, idx, indent + 2)

    myWrite('<symbol> ' + tokens[idx] + ' </symbol>', indent + 2)
    myWrite('</class>', indent)
    return idx + 1

folderName = sys.argv[1]
for fileName in os.listdir(folderName):
    if fileName.endswith('.jack'):
        input = './' + folderName + '/' + fileName
        print('./' + folderName + '/' + fileName[:-5] + '.xml')
        out = open('./' + folderName + '/' + fileName[:-5] + '.xml.bak', 'w')
        tokens = tokenize(input)
        true_tokens = handleStrings(tokens)
        parseClass(true_tokens, 0, 0)
