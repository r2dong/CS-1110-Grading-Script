from functools import partial
from inputGenerator import genElement
from fileUtility import *

# tests the provided function once
# inputs:
# func - <function> function to test
# stfName - <str> name of student's file
# solName - <str> name of solution file
# result:
# the passed in function object is updated with this test result
def testFunc(func, stfName, solName):
     
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
        times = function.testNum
        for dummy in range(0, times):
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