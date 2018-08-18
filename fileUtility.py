# This script was originally written by Willem Dejong. Rentian worked on
# improving style of the code and making a few improvements to functionality.

# Development Notes
# Correct Scores should be [[['jaalbaugh'], 0, 1, 0, 0, 1], [['ljcochrane'], 0, 1, 1, 1, 1]], and
# [[['edbuckley'], 0, 1, 1, 1, 1], [['tntrres'], 0, '0', '0', '0', '0']]

# to record name
import os
import re
import Newtester
import inputGenerator
import ast


# reads in the list of file/folders in path and make a list of .py files
def readFolder(path):
    # creates a list of items in the directory of path
    fileList = os.listdir(path)

    # removes testing .py codes from fileList, if they are in it
    if "tester.py" in fileList:
        fileList.remove("tester.py")
    if "readclass.py" in fileList:
        fileList.remove("readclass.py")
    if "solution.py" in fileList:
        fileList.remove("solution.py")

    # remove all none py file names from fileList
    index = 0  # loop index
    while index < len(fileList):
        # finds index of last '.' in file names. If no '.', it will be 0 and 
        # will check against the entire file name and fail. (unlesss it is a
        # folder named "py", so don't name a folder "py" in this directory.)
        try:
            fileExtIndex = fileList[index].rfind(".") + 1
        except:
            break
        # if it does not have a "py" as a the file extention remove from list
        if fileExtIndex == -1 or fileList[index][fileExtIndex:].lower() != "py":
            try:
                fileList.remove(fileList[index])
            except:
                print("Failed removing non-py file")
        else:
            index += 1

    # make all file names absolute paths
    absoluteFileList = []
    for fileName in fileList:
        absoluteFileList.append(fileName)

    # returns fileList containing only names of .py files
    return fileList


# stfResults is returned by Main.testFile
# writes at the end of the file
def writeComments(stfResults):
    for result in stfResults:
        absolutePath = result.path + "\\" + result.name

        # debug output
        print("Writing output to result " + absolutePath, flush=True)

        comments = str(result)
        comments = toggleComment(comments)
        stf = open(absolutePath, "a")
        stf.write("\n" + comments)
        stf.close()


# add "#" to each line of comment
def toggleComment(comment):
    comment = "# " + comment
    comment = comment.replace("\n", "\n# ")
    return comment


# remove the extension from a string file name
def removeExtension(fileName):
    extLoc = fileName.rfind(".")
    if extLoc == -1:
        # do nothing if file name has no extension
        return fileName
    else:
        return fileName[:extLoc]


# turn a csv into a matrix (list of list)
def csvToMatrix(csvFileName):
    file = open(csvFileName, "r")
    matrix = []
    for line in file:
        line = line.replace("\n", "")
        row = re.split(",", line)
        matrix.append(row)
    file.close()
    return matrix


# write a matrix into CSV file
def matrixToCsv(matrix, outFileName):
    strToWrite = ""
    for row in matrix:
        for element in row:
            strToWrite += str(element) + ","
        strToWrite += "\n"
    file = open(outFileName, "w")
    file.write(strToWrite)
    file.close()


# find column number of the specified header
def findColumn(matrix, colHeader):
    firstRow = matrix[0]
    col = 0
    for header in firstRow:
        if header == colHeader:
            return col
        else:
            col += 1
    # in case colHeader does not exist
    return -1


# convert a string to type using hard code
def stringToType(string):
    if string == "str":
        return str
    elif string == "int":
        return int
    elif string == "float":
        return float
    else:
        raise Exception("unidentified string to arg: " + string)


# convert an argument to argType from string to correct type
def stringToArg(string):
    delimiterPos = string.find(":")
    theType = string[:delimiterPos]
    arg = string[(delimiterPos + 1):]
    if theType == "int":
        return int(arg)
    elif theType == "float":
        return float(arg)
    elif theType == "str" or theType == "string":
        return arg
    elif theType == "boolean":
        return stringToBool(string)
    else:
        raise Exception("Unable to parse string to arg: " + arg)


# helper function to convert command line arguments to Ture/False in Python
def stringToBool(myString):
    myString = myString.lower()
    if myString in ("false", "0"):
        return False
    else:
        return True


# fName: full path to file to be parsed
def parseFuncSpec(fileName):
    funcs = []
    file = open(fileName, "r")

    for line in file:

        line = line.replace("\n", "")
        args = line.split(" ")

        # debug output
        print("Parsing line: " + line, flush=True)

        # create function
        if "function" in line:
            funcName = args[1]
            numTest = int(args[2])
            try:
                score = args[3]
            except:
                score = 1
            curFunc = Newtester.function(funcName, numTest, [], score)
            funcs.append(curFunc)
        # add inputs for the function
        else:
            if args[0] == "fixed":  # case of fixed set input
                args = args[1:]
                vals = []
                for arg in args:
                    vals.append(ast.literal_eval(arg))
                # create the inputArg object
                curInput = inputGenerator.argType(type(args[0]), valSet=vals)
            # case of random input
            else:
                theType = stringToType(args[0])
                print("parse type " + args[0] + " as " + str(theType))
                typeArgs = args[1:]
                argsLength = len(typeArgs)
                for index in range(0, argsLength):
                    print("parsing argument: " + typeArgs[index])
                    typeArgs[index] = stringToArg(typeArgs[index])
                print("creating new random input with type: " + str(theType) + " and args: " + str(typeArgs),
                      flush=True)
                curInput = inputGenerator.argType(theType, typeArgs)

            # append the current input argument to the function
            curFunc.addInput(curInput)

    file.close()
    return funcs