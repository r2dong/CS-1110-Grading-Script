from traceback import format_exc
from functools import partial
from copy import deepcopy
from fileUtility import read_folder


# constants
SEPERATOR = '-' * 20


# test a single arg_set for given function, return test result instance
def test_one_arg_set(arg_set, stf_func, sol_func):
    for arg in arg_set:
        stf_func = partial(stf_func, deepcopy(arg))
        sol_func = partial(sol_func, deepcopy(arg))
    try:
        stf_return_val = stf_func()
        exception_str = None
    except:
        stf_return_val = None
        exception_str = format_exc()
    return ArgSetTestResult(arg_set, sol_func(), stf_return_val, exception_str)


def test_func(func, stf, sol_name):
    sft_func = getattr(__import__(stf.no_ext_file_name), func.name)
    sol_func = getattr(__import__(sol_name), func.name)
    func_result = FunctionTestResult(func.name)
    stf.function_test_results.append(func_result)
    for arg_set in func.arg_sets:  # set up function calls
        set_result = test_one_arg_set(arg_set, sft_func, sol_func)
        func_result.add_set_result(set_result)


# test all functions in a file
# inputs
# funcs - <[function]> all functions to test
# sol - <str> name of solution file
def test_file(funcs, stf, sol):
    for func in funcs:
        test_func(func, stf, sol)


class FunctionTestResult:
    def __init__(self, function_name):
        self.function_name = function_name
        self.arg_set_test_results = []

    def add_set_result(self, result):
        self.arg_set_test_results.append(result)

    def __str__(self):
        string = SEPERATOR + ' function: ' + self.function_name
        string += ' ' + SEPERATOR + '\n'
        num_tests = str(len(self.arg_set_test_results))
        string += num_tests + ' cases were tested\n'
        return string


class ArgSetTestResult:
    
    # constructor
    # inputs: inputs used in this test
    # expected: expected results
    # actual: actual results
    def __init__(self, inputs, expected, actual, exception_str):
        self.inputs = inputs
        self.expected = expected
        self.actual = actual
        self.exception_str = exception_str
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
        if self.exception_str is not None:
            strRep += "A runtime error occurred with the following message:\n"
            strRep += self.exception_str
        return strRep


def grade_files(paths, sol, funcs):
    # get all fileNames to be graded
    sections = []
    for path in paths:
        section = read_folder(path)
        sections.append(section)
        for student_file in section.student_files:
            test_file(funcs, student_file, sol)
    return sections
