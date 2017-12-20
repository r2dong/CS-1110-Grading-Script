# this file contains functions to generate randomnized input
import random

def genInt(args):
    
    # take needed input and discard the rest
    try:
        lowerBound = args[0]
        upperBound = args[1]
    except:
        raise Exception("Invalid argument")
    
    return random.randint(lowerBound, upperBound)

def genFloat(args):
    
    try:
        lowerBound = args[0]
        upperBound = args[1]
    except:
        raise Exception("Invalid argument")
    
    return random.random() * (upperBound - lowerBound) + lowerBound

def genStr(args):
    
    # given pool to choose from
    if type(args[2]) == str:
        length = args[0]
        hasDuplicate = args[1]
        charPool = args[2]
    else:
        # take needed inputs and discard the rest
        try:
            length = args[0]
            hasDuplicate = args[1]
            hasUpper = args[2]
            hasLower = args[3]
            hasSymbol = args[4]
            
        except:
            raise Exception("Invalid input arguments")
        
        charPool = "" # possible characters to select from
        upperCaseLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        lowerCaseLetters = "qwertyuiopasdfghjklzxcvbnm"
        symbols = "`[]\;',./~!@#$%^&*()_+{}|:\"<>?"
        if hasUpper:
            charPool += upperCaseLetters
        if hasLower:
            charPool += lowerCaseLetters
        if hasSymbol:
            charPool += symbols
    
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

# let elementType be a string in the form of [[list, length], [list, length], ..., [int/decimal/string, args]]
def genElement(types):
    
    # recursive case
    if types[0][0] == list:
        curList = []
        length = types[0][1]
        for i in range(0, length):
            curList.append(genElement(types[1:]))
        return curList
    # base cases
    else:
        return genSingleElement(types[0])

def genSingleElement(types):
    
    # types are limited so hard-coded
    args = types[1] # list of arguments
    if types[0] == int:
        func = genInt
    elif types[0] == float:
        func = genFloat
    elif types[0] == str:
        func = genStr
    
    # generate random elements
    return func(args)

class argType:
    
    # constructor
    def __init__(self, theType, args):
        self.theType = theType
        self.args = args
    
    # get a value of this element
    def getValue(self):
        types = (self.theType, self.args)
        return genSingleElement(types)
    
                
                
            
            