from Newtester import *
import fileUtility
import sys
import argparse
import copy

# information on input arguments to functions to be tested
func_spec_file_name = "C:/Users/Rentian Dong/Desktop/Improving Grading Script/testEnvironment/inputFuncSpecs.txt"


# first parse command line arguments
# -p: paths to folders containing files to be tested (path)
# -s: path to correct implementation (solution)
# -o: customized output method, optional (output)
# -a: optional arguments required by specified output method (additional)
# -i: whether inputs to functions of all files should be the same, arguments are
#     parsed as strings and converted to bool later by function "stringToBool".
#     Was not able to find a more native solution from google.
def main():
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", nargs="+", dest="paths", type=str)
    parser.add_argument("-s", nargs=1, dest="sol", type=str)
    parser.add_argument("-o", nargs="?", dest="outMethod", type=str)
    parser.add_argument("-a", nargs="*", dest="optArgs", type=str)
    parser.add_argument("-i", nargs=1, dest="isIdentical", type=str)
    cmdArgs = parser.parse_args()

    # parse function input information from file
    # (this file should remain the same for all calls, just a way to pass in
    # information regarding functions, so we may use the same file name)
    funcs = fileUtility.parseFuncSpec(func_spec_file_name)

    # turn random inputs into fixed inputs if required
    if cmdArgs.isIdentical is None:
        isIdentical = fileUtility.stringToBool(cmdArgs.isIdentical[0])
    else:
        isIdentical = False
    if isIdentical:
        randomToFixed(funcs)

    # debug output
    print("Functions to be tested are:", flush=True)
    for func in funcs:
        print(func.name + " " + str(func.testNum), flush=True)

    # run all tests
    stfResults = gradeFiles(cmdArgs.paths, cmdArgs.sol, funcs)
    writeComments(stfResults)

    # write output using provided method
    if not len(cmdArgs.outMethod) == 0:
        index = 0
        for _ in cmdArgs.optArgs:
            cmdArgs.optArgs[index] = stringToArg(cmdArgs.optArgs[index])
            index += 1
        outMethod = __import__(cmdArgs.outMethod)
        outMethod.writeOutput(stfResults, cmdArgs.optArgs)


# gradeFiles tests all given homework files
#
# inputs:
# paths: list of paths containing all .py homework files
# hwIDs: list of columns headers of this homework in ICON exported .csv
# inputGradeSheets: path to ICON exported CSV
# outputGradeSheets: path to output CSV files
# solutionFileName: name of solution file
# homeworkContents: function names and their inputs
def gradeFiles(paths, sol, funcs):
    # get all fileNames to be graded
    stfResults = []
    for path in paths:
        # add paths to system search paths
        sys.path.insert(0, path)
        files = readFolder(path)
        for stf in files:
            funcsCopy = []
            for func in funcs:
                aCopy = copy.deepcopy(func)
                print("appending copy of " + aCopy.name + " to " + stf, flush=True)
                funcsCopy.append(aCopy)

            stfResult = StudentFile(stf, path, funcsCopy)
            stfResults.append(stfResult)
            testFile(stfResult.funcs, stfResult.name, sol)
    return stfResults


# helper function to convert random inputs to fixed inputs
def randomToFixed(funcs):
    for func in funcs:
        for arg in func.inputTypes:
            valSet = []
            for index in range(0, func.testNum):
                valSet.append(arg.getValue())
            arg.isFixedSet = True
            arg.valSet = valSet


class StudentFile:

    # constructor
    # inputs:
    # funcs - <[function]> functions tested, results added later
    # name - <str> absolute path to the file
    def __init__(self, name, path, funcs):
        self.name = name
        self.path = path
        self.funcs = funcs

    # print test results of this file
    def __str__(self):
        strRep = ""
        strRep += "FileName: " + self.name + "\n"
        for func in self.funcs:
            strRep += func.allTestsToStr() + "\n"
        return strRep


if __name__ == '__main__':
    main()
