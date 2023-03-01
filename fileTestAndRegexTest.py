import re

#test with files bringing in multiple variables with a file

def getStuff(file):
    dic={}
    with open(file,'r') as f:
        for line in f:
            line = line.strip('\n')
            name,age,exp,title = line.split(',')
            dic[name]= age+' Years old',exp + ' months experience',' as '+title
    return dic

# Print the passed dictionary
def dostuff(dic):
    for name in dic:
        print(name, dic[name])

# custom pattern with a period and then a pattern of choice by user

def searchPattern(file):
    cellPattern = re.compile(r'\d{3}.\d{3}.\d{4}')     # Grabs all patterns of numnumnum ANYTHING numnumnum ANYTHING numnumnumnum
    onlyDashDot = re.compile(r'\d{3}[-.]\d{3}[-.]\d{3}')   # grabs only ones with - or . between the nums
    only800900 = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}') # only grabs numbers that begin with 800 or 900
    prefixTag = re.compile(r'M(r|s|rs|iss)(\.)?\s[A-Z]\w*')   # match names with titles in the front such as mr mrs or ms
    with open(file,'r') as f:
        text = f.read()
        matches = cellPattern.finditer(text)
        matches2 = onlyDashDot.finditer(text)
        matches3 = only800900.finditer(text)
        for match in matches or matches2 or matches3:
            print(match)
        matches4 = prefixTag.finditer(text)
        for match in matches4:
            print(match)
    f.close()


def main():
    dic=getStuff('testtext.txt')
    dostuff(dic)
    print('------------------------')
    searchPattern('uhhh.txt')



main()