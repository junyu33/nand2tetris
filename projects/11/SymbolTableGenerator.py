import xml.etree.ElementTree as ET
import sys, os
folderName = sys.argv[1]
cnt = 0

def traverse(root, isDeclared):
    '''name;
    category (field, static, local, arg, class, subroutine);
    index: if the identifier's category is field, static, local, or arg,
    the running index assigned to the identifier by the symbol table;
    usage: whether the identifier is presently being declared (in a static / field / var variable declaration,
    or in a parameter list), or used (in an expression).
    '''
    for child in root:
        if child.tag == "identifier":
            name = child.text
            
            if root[0].text == ' var ':
                category = 'local'
            elif root[0].text == ' static ':
                category = 'static'
            elif root[0].text == ' field ':
                category = 'field'
            elif root[0].text == ' argument ':
                category = 'arg'
            elif root[0].text in [' constructor ', ' function ', ' method ']:
                category = 'subroutine'
            else:
                category = 'class'
            

            if category in [' field ', ' static ', ' local ', ' arg ']:
                index = str(cnt)
                cnt += 1
            else:
                index = 'false'
                cnt = 0
            
            usage = isDeclared
            child.text = name + category + " " + index + " " + usage
        
        if child.tag == 'subroutineBody':
            isDeclared = 'used'
            traverse(child, isDeclared)
        else:
            traverse(child, isDeclared)

        
        
for fileName in os.listdir(folderName):
    if fileName.endswith(".xml"):
        tree = ET.parse('./' + folderName + '/' + fileName)
        root = tree.getroot()
        traverse(root, 'declared')
        tree.write('./' + folderName + '/' + fileName[:-4] + '.symbol')