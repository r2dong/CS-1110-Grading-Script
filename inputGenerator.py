# input generator generates random inupt of specified types

# input types
#   - integer
#   - float
#   - string
#   - list of elements
#       - elements can be any type

import random

# myList should have a field as a list of myElements

class myElement:
    pass

def genInt(args):
    
    # take needed input and discard the rest
    try:
        lowerBound = args[0]
        upperBound = args[1]
    except:
        raise Exception("Invalid argument")
    
    return random.randint(lowerBound, upperBound)

def genDecimal(args):
    
    try:
        lowerBound = args[0]
        upperBound = args[1]
    except:
        raise Exception("Invalid argument")
    
    return random.random() * (upperBound - lowerBound) + lowerBound

def genString(args):
    
    # take needed inputs and discard the rest
    try:
        length = args[0]
        hasUpper = args[1]
        hasLower = args[2]
        hasSymbol = args[3]
        hasDuplicate = args[4]
    except:
        raise Exception("Invalid input arguments")
    
    charPool = "" # possible characters to select from
    if hasUpper:
        charPool += "QWERTYUIOPASDFGHJKLZXCVBNM"
    if hasLower:
        charPool += "qwertyuiopasdfghjklzxcvbnm"
    if hasSymbol:
        charPool += "`[]\;',./~!@#$%^&*()_+{}|:\"<>?"
    
    # build the random string
    randString = ""
    poolLength = len(charPool)
    while length > 0:
        nextIndex = random.randint(0, poolLength - 1)
        nextChar = charPool[nextIndex]
        # exclude duplicates if required
        if not hasDuplicate:
            if nextChar in randString:
                continue
        randString += nextChar
        length -= 1
    return randString

# let elementType be a string in the form of [list, list, ..., [int/decimal/string, args]]
def genList(length, types):
    
    curLength = length[0]
    curList = []
    # recursive case
    if len(length) > 1:
        for i in range(0, curLength):
            for i in range(0, curLength):
                curList.append(genList(length[1:], types))
            return curList
    # base cases
    else:
        args = types[1] # list of arguments
        if types[0] == int:
            func = genInt
        elif types[0] == float:
            func = genDecimal
        elif types[0] == str:
            func = genString
        
        # generate random elements
        for index in range(0, curLength):
            curList.append(func(args))
        return curList
            
                
                
            
            