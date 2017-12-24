from inputGenerator import argType
from Newtester import function
from Newtester import testFile
from fileUtility import *
import sys
import argparse

#**********************************************************************************************************************************
#These are to be changed as needed

# list containing integers representing the section(s) to skip
skipsections=[1, 2, 3, 4, 5]

#PATH is the path to the folder containing all the .py files
PATH1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/file"
PATH2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/file"
PATH3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/file"
PATH4="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/4"
PATH5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/file"
PATH6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6"
PATH7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7"

# number of problem for this assignment
NUMPROB = 4

# HWID is the string that matches exactly the header of the column that you are adding scores to in the icon exported csv
#HWID1="DA 2 Final Submission (540834)"
#HWID2="DA 2 Final Submission (547156)"
#HWID3="DA 2 Final Submission (547323)"
#HWID4="DA 2 Final Submission (548734)"
#HWID5="DA 2 Final Submission (549085)"
#HWID6="DA 2 Final Submission (548736)"
#HWID7="DA 2 Final Submission (548738)"

##INFILE is the path to the icon exported csv that you are reading from
#INFILE1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/05_Sep_20_20_Grades-CS_1110_0A01_Fall17.csv"
#INFILE2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/05_Sep_20_24_Grades-CS_1110_0A02_Fall17.csv"
#INFILE3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/05_Sep_20_26_Grades-CS_1110_0A03_Fall17.csv"
#INFILE4="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/4/05_Sep_20_27_Grades-CS_1110_0A04_Fall17.csv"
#INFILE5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/05_Sep_20_28_Grades-CS_1110_0A05_Fall17.csv"
#INFILE6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6/05_Sep_20_29_Grades-CS_1110_0A06_Fall17.csv"
#INFILE7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7/05_Sep_20_31_Grades-CS_1110_0A07_Fall17.csv"

##OUTFILE is the path to the csv file you wish to create/overwrite with the INFILE + added scores
#OUTFILE1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/newGrades1.csv"
#OUTFILE2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/newGrades2.csv"
#OUTFILE3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/newGrades3.csv"
#OUTFILE4="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/4/newGrades4.csv"
#OUTFILE5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/newGrades5.csv"
#OUTFILE6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6/newGrades6.csv"
#OUTFILE7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7/newGrades7.csv"

##**********************************************************************************************************************************


## main function
#if 1 not in skipsections:
    #clist=readfolder(PATH1) # list of py files in the directory
    #gradesList=runtester(clist,HWID1,INFILE1,OUTFILE1,PATH1)
    #removeExtraCol(OUTFILE1,HWID1)
#if 2 not in skipsections:
    #clist=readfolder(PATH2)
    #gradesList=runtester(clist,HWID2,INFILE2,OUTFILE2,PATH2)
    #removeExtraCol(OUTFILE2,HWID2)
#if 3 not in skipsections:
    #clist=readfolder(PATH3)
    #gradesList=runtester(clist,HWID3,INFILE3,OUTFILE3,PATH3)
    #removeExtraCol(OUTFILE3,HWID3)
#if 4 not in skipsections:
    #clist=readfolder(PATH4)
    #print(clist)
    #gradesList=runtester(clist,HWID4,INFILE4,OUTFILE4,PATH4)
    #removeExtraCol(OUTFILE4,HWID4)
#if 5 not in skipsections:
    #clist=readfolder(PATH5)
    #gradesList=runtester(clist,HWID5,INFILE5,OUTFILE5,PATH5)
    #removeExtraCol(OUTFILE5,HWID5)
#if 6 not in skipsections:
    #clist=readfolder(PATH6)
    #gradesList=runtester(clist,HWID6,INFILE6,OUTFILE6,PATH6)
    #removeExtraCol(OUTFILE6,HWID6)
#if 7 not in skipsections:
    #clist=readfolder(PATH7)
    #gradesList=runtester(clist,HWID7,INFILE7,OUTFILE7,PATH7)
    #removeExtraCol(OUTFILE7,HWID7)

funcInputFile = "C:/Users/Rentian Dong/Desktop/inputFuncSpecs.txt"

# first parse command line arguments
# -p: paths to folders containing files to be tested
# -s: path to correct implementation
# -o: customized output method, optional
# -a: optional arguments required by specified output method
def main():
    
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", nargs = "+", dest = "paths", type = str)
    parser.add_argument("-s", nargs = 1, dest = "sol", type = str)
    parser.add_argument("-o", nargs = "?", dest = "outMethod", type = str)
    parser.add_argument("-a", nargs = "*", dest = "optArgs", type = str)
    cmdArgs = parser.parse_args()
    
    # parse function input information from file
    funcs = parseFuncSpec(funcInputFile)
    
    # run all tests
    stfResults = gradeFiles(cmdArgs.paths, cmdArgs.sol, funcs)
    for result in stfResults:
        print(str(result))    
    writeComments(stfResults)
    
    # write output using provided method
    if not len(cmdArgs.outMethod) == 0:
        index = 0
        for arg in cmdArgs.optArgs:
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
                funcsCopy.append(func.copy()) 
            stfResult = studentFile(stf, path, funcsCopy)
            stfResults.append(stfResult)
            testFile(stfResult.funcs, stfResult.name, sol)
    return stfResults

class studentFile:
    
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

# some simple test cases
path = "C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/testPath/"
paths = [path]
sol = "solution_file.py"
int11 = argType(int, [0, 100])
int12 = argType(int, [0, 100])
int13 = argType(int, [0, 100])
int14 = argType(int, [0, 100])
midPointFunc = function("getMidpoint", 2, [int11, int12, int13, int14])
int21 = argType(int, [0, 100])
int22 = argType(int, [0, 100])
int23 = argType(int, [0, 100])
int24 = argType(int, [0, 100])
int25 = argType(int, [0, 100])
getAvgFunc = function("getAverage", 2, [int21, int22, int23, int24, int25])
getAvgStrFunc = function("getAverageString", 2, [int21, int22, int23, int24, int25])
int41 = argType(int, [0, 10])
int42 = argType(int, [0, 10])
str41 = argType(str, [1, True, "HS"])
getLengthFunc = function("getLength", 2, [int41, int42, str41])
funcs = [midPointFunc, getAvgFunc, getAvgStrFunc, getLengthFunc]
outFile = "C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/4/newGrades4.csv"
hwID = "DA 2 Final Submission (548734)"
inFile = "C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/4/05_Sep_20_27_Grades-CS_1110_0A04_Fall17.csv"

# main(paths, sol, funcs, "introToCS", outFile, hwID, inFile)
main()





