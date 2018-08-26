""" this file contains functions to read functions specs, student files, and write grading output to file """

import os
import ast
import csv
from traceback import format_exc
from os.path import splitext
from shutil import copy
from os.path import basename
from os import makedirs
from Newtester import test_func
from Newtester import Func

# constants
NUM_PADDING = 5
NUM_META_ROWS = 4  # first n columns to copy from template grade sheet
GRADE_SHEET_FIRST_ROW = 'Student', 'ID', 'SIS Login ID', 'Section'
HAWK_ID_COL = 2  # column in template with hawkIDs


def get_all_hawk_ids(grade_sheet_file_name):
    """
    find all valid hawk_ids from a grade sheet
    :param grade_sheet_file_name: path to a grade sheet
    :return: a list of strings, with all hawk ids from the given grade sheet
    """
    with open(grade_sheet_file_name) as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        return [row[HAWK_ID_COL] for row in reader]


def read_folder(folder_name):
    """
    reads a folder containing submissions of a single section
    :param folder_name: folder to be read
    :return: a Section instance
    """

    file_names = os.listdir(folder_name)
    section = Section(folder_name)

    for file_name in file_names:
        _, ext = splitext(file_name)
        if ext == '.csv':
            file_name = os.path.join(folder_name, file_name)
            valid_hawk_ids = get_all_hawk_ids(file_name)
            break

    for file_name in file_names:
        _, ext = splitext(file_name)
        if ext == '.csv':
            section.template_name = file_name
        else:
            # noinspection PyUnboundLocalVariable
            section.add_file(StudentFile(folder_name, file_name, valid_hawk_ids))

    return section


def parse_func_specs(fileName):
    """
    parse a func spec file into Function instances
    :param fileName: path of function spec file
    :return: a list of Function instances
    """
    funcs = []
    is_last = False
    with open(fileName) as file:
        reader = csv.reader(file)
        while not is_last:
            next_func, is_last = parse_one_func(reader)
            funcs.append(next_func)
    return funcs


def parse_one_func(reader):
    """
    read one function out of spec file
    :param reader: csv reader on the func spec file
    :return: a single Function instance
    """

    # meta info of function
    is_last = False
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
        try:
            row = next(reader)
        except StopIteration:
            is_last = True
            break

    return Func(name, arg_sets, score), is_last


class Section:
    """ instance representing all submissions of a single section """

    def __init__(self, folder_name):
        self.student_files = []
        self.template_name = None
        self.folder_name = folder_name

    def grade_section(self, sol_fname, funcs):
        """
        grade all submissions of this section
        :param sol_fname: path of solution file
        :param funcs: list of Function instances specifying function specs
        """
        for stf in self.student_files:
            for func in funcs:
                test_func(func, stf, sol_fname)

    def add_file(self, file):
        """
        add a new StudentFile instance
        :param: file: a StudnetFile instance
        """
        self.student_files.append(file)

    def write_test_results(self, out_dir):
        """
        write test feedback to all student files in this section
        :param out_dir: destination directory to place the new files
        """
        for student_file in self.student_files:
            student_file.write_test_results(os.path.join(out_dir, basename(self.folder_name)))

    def __get_total_score(self, hwid):
        full_path = os.path.join(self.folder_name, self.template_name)
        with open(full_path) as file:
            reader = csv.reader(file)
            first_row = next(reader)
            for i in range(0, len(first_row)):
                if first_row[i] == hwid:
                    score_col = i
            score_row = next(reader)
            # noinspection PyUnboundLocalVariable
            return score_row[score_col]

    # get a score using hawk id, or return none if id does not exist
    def __score_by_id(self, hawk_id):
        for stf in self.student_files:
            if hawk_id == stf.hawk_id:
                return stf.calc_score()

    def write_grade_sheet(self, out_dir, hwid):
        """ write the grade sheet for this section """

        first_row = GRADE_SHEET_FIRST_ROW + (hwid,)
        total_score = self.__get_total_score(hwid)
        second_row = ['Points Possible'] + [''] * (NUM_META_ROWS - 1) + \
                     [str(total_score)]
        template_file_name = os.path.join(self.folder_name, self.template_name)
        out_file_name = os.path.join(out_dir, basename(self.folder_name), basename(self.template_name))

        with open(out_file_name, 'w') as out_file, \
                open(template_file_name, 'r') as template_file:

            writer = csv.writer(out_file, lineterminator='\n')
            writer.writerow(first_row)
            writer.writerow(second_row)
            template_file_reader = csv.reader(template_file)
            next(template_file_reader)  # skip first two rows of template
            next(template_file_reader)

            for row in template_file_reader:
                hawk_id = row[HAWK_ID_COL]
                score = self.__score_by_id(hawk_id)
                row = row[:NUM_META_ROWS]
                if score is not None:
                    row += [str(score)]
                writer.writerow(row)


class StudentFile:
    """ represents a single submission from a student """

    def __init__(self, folder_name, file_name, valid_ids):
        self.path = os.path.join(folder_name, file_name)
        self.folder_name = folder_name
        self.full_file_name = file_name
        self.no_ext_file_name = file_name[:-3]
        self.hawk_id_exc_str = None
        self.hawk_id_err = None
        self.function_test_results = []
        self.__validate_hawk_id(valid_ids)

    def __validate_hawk_id(self, valid_ids):
        # noinspection PyBroadException
        try:
            self.hawk_id = __import__(self.no_ext_file_name).getHawkIDs()[0]
        except Exception:
            self.hawk_id = None
            err_str = format_exc()
            err_str = err_str[err_str.rfind('\n', 0, len(err_str) - 1) + 1:]
            self.hawk_id_exc_str = err_str
        if self.hawk_id not in valid_ids:
            self.hawk_id_err = True

    # append test results as comments at back of file
    def write_test_results(self, out_dir):
        """
        make a copy of the student submission, then write feedbacks as comments to the end
        :param out_dir: output destination of the grade sheet
        """
        string = ''
        if self.hawk_id_exc_str is not None:
            string += 'something wrong happend when reading your getHawkIDs function:\n'
        elif self.hawk_id_err:
            string += 'could not find a match for the hawk id you returned in getHawkIDs function\n'
            string += 'please double check you spelled it right\n'
        for func_result in self.function_test_results:
            string += str(func_result) + '\n'
            for i in range(0, len(func_result.arg_set_test_results)):
                string += 'case: ' + str(i) + ':\n'
                string += str(func_result.arg_set_test_results[i]) + '\n' * 2
        makedirs(out_dir, exist_ok=True)
        old_file_name = os.path.join(self.folder_name, self.full_file_name)
        new_file_name = os.path.join(out_dir, self.full_file_name)
        path = copy(old_file_name, new_file_name)
        with open(path, 'a') as file:
            file.write('\n' * NUM_PADDING)
            file.write((lambda s: '# ' + s.replace("\n", "\n# "))(string))

    def calc_score(self):
        """
        calculate the score of this student
        :return: the score
        """
        score = 0
        for result in self.function_test_results:
            score += result.calc_score()
        return score
