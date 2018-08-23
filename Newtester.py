from traceback import format_exc
from functools import partial
from copy import deepcopy
from stopit import ThreadingTimeout
import stopit


# constants
SEPERATOR = '-' * 15
TIMEOUT_SEC = 5
INFINITE_LOOP_STR = 'Function not finished within 5 seconds, ' \
                    'very likely due to infinite loops\n'
FUNC_TEST_HEADER = '-' * 15 + ' function: %s, score: %d \
                      /%d' + '-' * 15 + '\n'


def run_with_timeout(func):
    with ThreadingTimeout(TIMEOUT_SEC):
        exc_str = None
        return_val = None
        time_out = False
        # noinspection PyBroadException
        try:
            return_val = func()
        except stopit.utils.TimeoutException:
            time_out = True
        except Exception:
            exc_str = format_exc()
    return time_out, return_val, exc_str


# test a single arg_set for given function, return test result instance
def test_one_arg_set(arg_set, stf_func, sol_func):
    for arg in arg_set:
        stf_func = partial(stf_func, deepcopy(arg))
        sol_func = partial(sol_func, deepcopy(arg))
    is_timeout, return_val, exc_str = run_with_timeout(stf_func)
    answer_key = sol_func()
    ArgSet_partial = partial(ArgSetTestResult, arg_set, answer_key)
    if is_timeout:
        return ArgSet_partial(None, INFINITE_LOOP_STR)
    elif exc_str:
        return ArgSet_partial(None, exc_str)
    else:
        return ArgSet_partial(return_val, None)


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
            score_recieved = 0
            body = self.exc_str
        else:
            score_recieved = self.score
            num_tests = str(len(self.arg_set_test_results))
            body = num_tests + ' cases were tested\n'
        header = FUNC_TEST_HEADER % (self.function_name, score_recieved, self.score)
        return header + body


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


def grade_section(sol_fname, funcs, section):
    for stf in section.student_files:
        for func in funcs:
            test_func(func, stf, sol_fname)


class Func:

    # constructor
    # inputs:
    # name - <str> name of function
    # score - <int> points rewarded for correct function
    def __init__(self, name, arg_sets, score):
        self.name = name
        self.arg_sets = arg_sets
        self.score = score
        self.testResults = []
