import os
import re
from copy import deepcopy
import ast
import csv

# constants
NUM_PADDING = 5


# reads a folder containing submissions of a single section
def read_folder(folder_name):
    file_names = os.listdir(folder_name)
    section = Section()
    for file_name in file_names:
        section.add_file(StudentFile(folder_name, file_name))
    return section


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
def parse_func_specs(fileName):
    funcs = []
    with open(fileName) as file:
        reader = csv.reader(file, lineterminator='\n')
        while True:
            try:
                funcs.append(parse_one_func(reader))
            except StopIteration:
                return funcs


# helper function that read one function out of spec file
def parse_one_func(reader):

    # meta info of function
    row = next(reader)
    name = row[0]
    try:
        score = row[1]
    except IndexError:
        score = 1

    # all input sets of function
    arg_sets = []
    row = next(reader)
    while len(row) != 0:
        cur_arg_set = []
        for arg in row:
            cur_arg_set.append(ast.literal_eval(arg))
        arg_sets.append(cur_arg_set)
        row = next(reader)

    return Func(name, arg_sets, score)


class Section:
    def __init__(self):
        self.student_files = []

    # add a new StudentFile instance
    def add_file(self, file):
        self.student_files.append(file)

    # write test feedback to all student files in this section
    def write_feedback(self):
        for student_file in self.student_files:
            student_file.write_feedback()


class StudentFile:

    # constructor
    # inputs:
    # funcs - <[function]> functions tested, results added later
    # name - <str> absolute path to the file
    def __init__(self, folder_name, file_name):
        self.path = os.path.join(folder_name, file_name)
        self.folder_name = folder_name
        self.full_file_name = file_name
        self.no_ext_file_name = file_name[:-3]
        # sys.path.append(folder_name)
        self.hawk_id = __import__(self.no_ext_file_name).getHawkIDs()
        self.function_test_results = []

    # append test results as comments at back of file
    def write_feedback(self):
        string = ''
        for func_result in self.function_test_results:
            string += str(func_result) + '\n'
            for i in range(0, len(func_result.arg_set_test_results)):
                string += 'case: ' + str(i) + ':\n'
                string += str(func_result.arg_set_test_results[i]) + '\n' * 2
        with open(self.path, 'a') as file:
            file.write('\n' * NUM_PADDING)
            file.write((lambda s: '# ' + s.replace("\n", "\n# "))(string))


class Func:

    # constructor
    # inputs:
    # name - <str> name of function
    # testNum - <int> number of times to test function
    # inputTypes - <[argType]> types of input arguments of function
    # score - <int> points rewarded for correct function
    def __init__(self, name, arg_sets, score):
        self.name = name
        self.arg_sets = arg_sets
        self.score = score
        self.testResults = []

    # add a new test result to this function
    def addResult(self, result):
        self.testResults.append(result)

    # add a new set of inputs to this function
    def addInput(self, arg_list):
        self.arg_sets.append(arg_list)

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
        return Func(self.name, deepcopy(self.arg_sets), self.score)
