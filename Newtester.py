from functools import partial
from inputGenerator import *
from fileUtility import *
import copy

# tests the provided function once
# inputs:
# func - <function> function to test
# stfName - <str> name of student's file
# solName - <str> name of solution file
# result:
# the passed in function object is updated with this test result
def testFunc(func, stfName, solName):
    
    stfName = removeExtension(stfName)
    solName = removeExtension(stfName)
    stfFunc = getattr(__import__(stfName), func.name)
    solFunc = getattr(__import__(solName), func.name)
    inputs = []
    inputTypes = func.inputTypes
    for theType in inputTypes:
        nextArg = theType.getValue()
        # if pass by reference, create a copy for two functions
        try:
            nextArg1 = nextArg.copy()
            nextArg2 = nextArg.copy()
            inputs.append(nextArg.copy())
        except:
            nextArg1 = nextArg
            nextArg2 = nextArg
            inputs.append(nextArg)
        stfFunc = partial(stfFunc, nextArg1)
        solFunc = partial(solFunc, nextArg2)
        
    # run both functions
    keySol = solFunc()
    try:
        keyStf = stfFunc()
    except:
        keyStf = None
        
    # update test result
    result = testResult(inputs, keySol, keyStf)
    func.addResult(result)

# test all functions in a file
# inputs
# funcs - <[function]> all functions to test
# stf - <str> name of student's file
# sol - <str> name of solution file
def testFile(funcs, stf, sol):
    for func in funcs:
        times = func.testNum
        for index in range(0, times):
            print("Testing " + func.name + " " + str(index), flush = True)
            testFunc(func, stf, sol)

class function:
    
    # constructor
    # inputs:
    # name - <str> name of function
    # testNum - <int> number of times to test function
    # inputTypes - <[argType]> types of input arguments of function
    # score - <int> points rewarded for correct function
    def __init__(self, name, testNum, inputTypes, score = 1):
        self.name = name
        self.testNum = testNum
        self.inputTypes = inputTypes
        self.score = score
        self.testResults = []
    
    # add a new test result to this function
    def addResult(self, result):
        self.testResults.append(result)
    
    # add a new input argument to this function
    def addInput(self, arg):
        self.inputTypes.append(arg)
    
    # return string representation of all tests done on this function
    def allTestsToStr(self):
        strRep = ""
        strRep += self.name + "\n"
        numOfTests = len(self.testResults)
        strRep += str(numOfTests) + " tests done:\n"
        for testNum in range(0, numOfTests):
            strRep += "test #" + str(testNum) + "\n"
            strRep += str(self.testResults[testNum]) + "\n\n"
        return strRep
    
    # make a copy of this function, excludes test results
    def copy(self):
        return function(self.name, self.testNum, self.inputTypes, self.score)
        

# testResult should alwasy be used with a corresponding function
class testResult:
    
    # constructor
    # inputs: inputs used in this test
    # expected: expected results
    # actual: actual results
    def __init__(self, inputs, expected, actual):
        self.inputs = inputs
        self.expected = expected
        self.actual = actual
        self.isCorrect = expected == actual
    
    # to return a string representation of this test result
    def __str__(self):
        strRep = ""
        inputStr = str(self.inputs).replace("[", "(")
        inputStr = inputStr.replace("]", ")")
        strRep += "Inputs: " + inputStr + "\n"
        strRep += "Expected: " + str(self.expected) + "\n"
        strRep += "Actual: " + str(self.actual) + "\n"
        if self.isCorrect:
            strRep += "passed"
        else:
            strRep += "failed"
        return strRep

# simple test cases
#int1 = argType(int, [0, 100])
#int2 = argType(int, [0, 100])
#SorH = argType(str, [1, True, "HS"])
#getLengthFunc = function("getLength", 2, [int1, int2, SorH])
#allFuncs = [getLengthFunc]
#stfName = "C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/testPath/granillovelasqukenneth_47840_4611593_GranilloVelasquezKennethDA2-2"
#solName = "solution_file"
#testFile(allFuncs, stfName, solName)
#print(getLengthFunc.allTestsToStr())

