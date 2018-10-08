"""
this file contains functions to read functions specs,
student files, and write grading output to file
"""

import os
import csv
from os.path import splitext
from os.path import dirname
from shutil import copy
from os.path import basename
from os import makedirs
from Tester import test_func
from Tester import Func
from ast import literal_eval

# constants
NUM_HEADER_ROWS = 2  # #header rows in grade sheet
NUM_PADDING = 5
NUM_META_ROWS = 4  # first n columns to copy from template grade sheet
GRADE_SHEET_FIRST_ROW = 'Student', 'ID', 'SIS Login ID', 'Section'
HAWK_ID_COL = 2  # column in template with hawkIDs
HAWK_ID_EXC_STR = 'something wrong happend when reading your getHawkIDs function\n' + \
                  'maybe there is a typo in function name?\n'
HAWK_ID_NON_EXIST_STR = 'could not find a match for the hawk id you returned in getHawkIDs function\n' + \
                        'maybe you did not spell it right?\n'
SEE_TA = 'Note that you are assigned a score of 0 for this\n' + \
         'Please discuss with a TA ASAP IN PERSON to recieve credit for this assignment\n'
SYNTAX_ERR = 'It appears that your file has a syntax error\n' + \
             'Be sure to click the GREEN ARROW in the upper middle before submitting\n' + \
             'and confirm you file loads without any syntax errors\n'
HAWK_ID_COMMENT = '#' * 15 + 'function: getHawkIDs, score: %d/1' + '#' * 15 + '\n'
OH = 'Have trouble completing this assignment? Get help during the following OH/Study Group Sessions:\n' \
     'APOORV ADITYA  (also requesting all queries over grading of discussion assignments) -:\n' \
     'Email:\n' \
     'apoorv-aditya@uiowa.edu\n' \
     '\n' \
     'Study groups-:\n' \
     'Monday 4:30 pm to 5:30 pm (301 MLH) \n' \
     'Tuesday 6 pm to 7 pm (301 MLH) \n' \
     '\n' \
     'Office hours-: \n' \
     'Mon 12:30 pm to 1:30 pm (101N MLH)\n' \
     'Tue 3:30 pm to 5:30 pm (101N MLH) \n' \
     ' \n' \
     'Rentian Dong  (direct all queries on Programming Assignment grading to him):\n' \
     'Email:\n' \
     'rentian-dong@uiowa.edu\n' \
     ' \n' \
     'Office hours:\n' \
     'Thur 6:00 pm to 7:00 pm (301 MLH)\n' \
     'Fri 3:30 pm - 5:30 pm (301 MLH) \n' \
     ' \n' \
     'Jessica Lu \n' \
     'Email:\n' \
     'jessica-lu@uiowa.edu\n' \
     '\n' \
     'Study groups:\n' \
     'Wednesday 6:30 pm to 7:30 pm (B13 MLH)\n' \
     'Thur 4pm to 5pm (B13 MLH) \n' \
     '\n' \
     'Office hours:\n' \
     'Wednesday 4:30 pm to 5:30 pm (301 MLH)\n' \
     'Friday  10am to 12pm (B13 MLH)\n'


def skip_elems(n, iterator):
    """
    skip n elements of an iterator
    islice method appears problematic for no obvious reason
    """
    for i in range(0, n):
        next(iterator)
    return iterator


def get_hawk_ids(grade_sheet_file_name):
    """
    find all valid hawk_ids from a grade sheet
    :param grade_sheet_file_name: path to a grade sheet
    :return: a list of strings, with all hawk ids from the given grade sheet
    """
    with open(grade_sheet_file_name) as file:
        reader = skip_elems(NUM_HEADER_ROWS, csv.reader(file))
        return [row[HAWK_ID_COL] for row in reader]


# noinspection PyShadowingNames
def read_folder(folder_name):
    """
    reads a folder containing submissions of a single section
    :param folder_name: folder to be read
    :return: a Section instance
    """

    # deal with grade sheet
    fnms = os.listdir(folder_name)  # file names
    path = list(filter(lambda fn: splitext(fn)[1] == '.csv', fnms))[0]
    path = os.path.join(folder_name, path)
    section = Section(folder_name, path)
    valid_hawk_ids = get_hawk_ids(path)

    # deal with all student submission files
    stfnms = list(filter(lambda fn: splitext(fn)[1] != '.csv', fnms))
    for fn in stfnms:
        if not fn == '__pycache__':
            section.add_file(StudentFile(folder_name, fn, valid_hawk_ids))

    return section


def parse_func_specs(fn):
    """
    parse a func spec file into Function instances
    :param fn: path of function spec file
    :return: a list of Function instances
    """
    funcs = []
    is_last = False
    with open(fn) as file:
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
        arg_sets.append([literal_eval(arg) for arg in row])
        try:
            row = next(reader)
        except StopIteration:
            is_last = True
            break

    return Func(name, arg_sets, score), is_last


class Section:
    """ instance representing all submissions of a single section """

    def __init__(self, folder_name, grade_sheet_name):
        self.student_files = []
        self.grade_sheet_name = grade_sheet_name
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
        os.chdir(out_dir)
        for student_file in self.student_files:
            student_file.write_test_results(basename(self.folder_name))

    def __get_total_score(self, hwid):
        full_path = os.path.join(self.folder_name, self.grade_sheet_name)
        with open(full_path) as file:
            reader = csv.reader(file)
            first_row = next(reader)
            score_row = next(reader)
            return score_row[first_row.index(hwid)]

    # get a score using hawk id, or return none if id does not exist
    def __score_by_id(self, hawk_id):
        for stf in self.student_files:
            if hawk_id == stf.hawk_id:
                return stf.score()

    # add "SIS User ID" column to output grade sheet, if missing
    @staticmethod
    def __fix_sis_user_id(fn):
        with open(fn) as f:
            reader = csv.reader(f)
            first_row = next(reader)
            if 'SIS_User_ID' in first_row:
                return
        with open(fn) as f:
            reader = csv.reader(f)
            all_rows = [r for r in reader]
            all_rows[0].insert(2, 'SIS User ID')
            for r in all_rows[1:]:
                r.insert(2, '')
        with open(fn, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(all_rows)

    def write_grade_sheet(self, out_dir, hwid):
        """ write the grade sheet for this section """

        first_row = GRADE_SHEET_FIRST_ROW + (hwid,)
        total_score = self.__get_total_score(hwid)
        second_row = ['Points Possible'] + [''] * (NUM_META_ROWS - 1) + [str(total_score)]
        tfn = os.path.join(self.folder_name, self.grade_sheet_name)  # grade sheet file name
        ofn = os.path.join(out_dir, basename(self.folder_name), basename(self.grade_sheet_name))  # out file name

        with open(ofn, 'w') as out_file, open(tfn, 'r') as template_file:

            writer = csv.writer(out_file, lineterminator='\n')
            writer.writerow(first_row)
            writer.writerow(second_row)
            tf_reader = skip_elems(NUM_HEADER_ROWS, csv.reader(template_file))

            for row in tf_reader:
                hawk_id = row[HAWK_ID_COL]
                score = self.__score_by_id(hawk_id)
                row = row[:NUM_META_ROWS]
                if score is not None:
                    row += [str(score)]
                else:
                    row += ['']
                writer.writerow(row)

        Section.__fix_sis_user_id(ofn)


class StudentFile:
    """ represents a single submission from a student """

    def __init__(self, folder_name, file_name, valid_ids):
        self.__full_path = os.path.join(folder_name, file_name)
        self.syntax_err = False
        self.hawk_id_exc_str = None  # exception ocurrs while getting hawk id
        self.hawk_id_err = False  # hawk id does not exist
        self.hawk_id = None
        self.function_test_results = []
        self.__validate_hawk_id(valid_ids)

    def __path(self):
        return self.__full_path

    def __folder(self):
        return dirname(self.__path())

    def __file_ext(self):
        return basename(self.__path())

    def file_xext(self):
        """ file name with out extension """
        name_ext = self.__file_ext()
        return name_ext[:name_ext.rfind('.')]

    def __validate_hawk_id(self, valid_ids):

        # noinspection PyBroadException
        try:  # first check if there is syntax error (if the file loads)
            __import__(self.file_xext())
        except Exception:
            self.syntax_err = True
            return

        # noinspection PyBroadException
        try:  # then check if getHawkIDs is syntax correct
            self.hawk_id = __import__(self.file_xext()).getHawkIDs()[0].lower()
        except Exception:
            self.hawk_id_exc_str = HAWK_ID_EXC_STR
            return

        if self.hawk_id not in valid_ids:  # finally check if hawk_id obtained is valid
            self.hawk_id_err = True

    def __hawk_id_comment(self):
        if self.hawk_id_exc_str:
            return HAWK_ID_COMMENT % 0 + self.hawk_id_exc_str + SEE_TA + '\n'
        elif self.hawk_id_err:
            return HAWK_ID_COMMENT % 0 + HAWK_ID_NON_EXIST_STR + SEE_TA + '\n'
        else:  # hawk id all good
            return HAWK_ID_COMMENT % 1 + '\n'

    def write_test_results(self, out_dir):
        """
        make a copy of the student submission, then write feedbacks as comments to the end
        :param out_dir: output destination of the grade sheet
        """
        makedirs(out_dir, exist_ok=True)
        new_fn = os.path.join(out_dir, self.__file_ext())
        path = copy(self.__path(), new_fn)
        if self.syntax_err:  # no need for comments if submission has syntax error
            string = SYNTAX_ERR + SEE_TA
        else:
            string = self.__hawk_id_comment()
            for func_result in self.function_test_results:
                string += str(func_result) + '\n' * 2
            string += '\n' * NUM_PADDING + OH
        with open(path, 'a') as file:
            file.write('\n' * NUM_PADDING)
            file.write((lambda s: '# ' + s.replace("\n", "\n# "))(string))

    def score(self):
        """
        calculate the score of this student
        :return: the score
        """
        score = 1
        if self.hawk_id_exc_str or self.hawk_id_err:
            score = 0
        for result in self.function_test_results:
            score += result.calc_score()
        return score
