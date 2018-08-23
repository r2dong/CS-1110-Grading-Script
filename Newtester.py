from traceback import format_exc
from functools import partial
from copy import deepcopy
from fileUtility import read_folder
from stopit import ThreadingTimeout


# constants
SEPERATOR = '-' * 15
TIMEOUT_SEC = 5
INFINITE_LOOP_ERR_STR = 'Function not finished within 5 seconds, very likely due to infinite loops\n'
# end of constants


# test a single arg_set for given function, return test result instance
# TODO refactor out testing of inifinite loops
def test_one_arg_set(arg_set, stf_func, sol_func):
    for arg in arg_set:
        stf_func = partial(stf_func, deepcopy(arg))
        sol_func = partial(sol_func, deepcopy(arg))
    with ThreadingTimeout(TIMEOUT_SEC) as time_out_ctx:
        # noinspection PyBroadException
        try:
            stf_return_val = stf_func()
        except Exception:
            exception_str = format_exc()
            return ArgSetTestResult(arg_set, sol_func(), None, exception_str)
    if time_out_ctx.state == time_out_ctx.TIMED_OUT:
        exception_str = INFINITE_LOOP_ERR_STR
    else:
        exception_str = None
    return ArgSetTestResult(arg_set, sol_func(), stf_return_val, exception_str)


def test_func(func, stf, sol_name):

    sol_func = getattr(__import__(sol_name), func.name)
    try:
        sft_func = getattr(__import__(stf.no_ext_file_name), func.name)
    except:
        func_result = FuncTestResult(func.name, func.score, format_exc())
        stf.function_test_results.append(func_result)
        return

    func_result = FuncTestResult(func.name, func.score, None)
    stf.function_test_results.append(func_result)
    for arg_set in func.arg_sets:  # set up function calls
        set_result = test_one_arg_set(arg_set, sft_func, sol_func)
        func_result.add_set_result(set_result)


# test all functions in a file
# inputs
# funcs - <[function]> all functions to test
# sol - <str> name of solution file
def test_file(funcs, stf, sol_name):
    for func in funcs:
        test_func(func, stf, sol_name)


class FuncTestResult:
    def __init__(self, function_name, score, exc_str):
        self.function_name = function_name
        self.score = score
        self.arg_set_test_results = []
        self.exc_str = exc_str

    def add_set_result(self, result):
        self.arg_set_test_results.append(result)

    def calc_score(self):
        score = self.score
        for set_result in self.arg_set_test_results:
            if not set_result.is_correct:
                score = 0
                break
        return score

    def __str__(self):
        if self.exc_str is not None:
            string = SEPERATOR + ' function: ' + self.function_name
            string += ', score: ' + '0' \
                      + '/' + str(self.score) + ' ' + SEPERATOR + '\n'
            string += self.exc_str
        else:
            string = SEPERATOR + ' function: ' + self.function_name
            string += ', score: ' + str(self.calc_score()) \
                      + '/' + str(self.score) + ' ' + SEPERATOR + '\n'
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
        self.is_correct = expected == actual
    
    # to return a string representation of this test result
    def __str__(self):
        strRep = ""
        inputStr = str(self.inputs).replace("[", "(")
        inputStr = inputStr.replace("]", ")")
        strRep += "Inputs: " + inputStr + "\n"
        strRep += "Expected: " + str(self.expected) + "\n"
        strRep += "Actual: " + str(self.actual) + "\n"
        if self.is_correct:
            strRep += "passed"
        else:
            strRep += "failed"
        if self.exception_str is not None:
            strRep += "A runtime error occurred with the following message:\n"
            strRep += self.exception_str
        return strRep


def grade_files(paths, hwids, sol, funcs):
    # get all fileNames to be graded
    sections = []
    total_score = 0
    for func in funcs:
        total_score += func.score
    for path, hwid in zip(paths, hwids):
        section = read_folder(path, hwid, total_score)
        sections.append(section)
        for student_file in section.student_files:
            test_file(funcs, student_file, sol)
    return sections
