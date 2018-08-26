""" entry point of grading script """

import fileUtility
import argparse
import sys
from os.path import dirname
from os.path import basename


def main():
    """ entry point of grading script """

    parser = argparse.ArgumentParser()  # parse command line arguments
    parser.add_argument('-p', nargs='+', dest='paths', type=str)  # section folders
    parser.add_argument('-i', nargs='+', dest='hwids', type=str)  # same order as section folders
    parser.add_argument('-s', dest='sol', type=str)  # solution file path
    parser.add_argument('-f', dest='spec', type=str)  # function spec file path
    parser.add_argument('-o', dest='out_dir', type=str)  # output directory
    cmdArgs = parser.parse_args()

    if len(cmdArgs.hwids) != 1 and len(cmdArgs.hwids) != len(cmdArgs.paths):
        raise Exception('invalid section folder and hwid input')
    if len(cmdArgs.hwids) == 1:
        the_id = cmdArgs.hwids[0]
        cmdArgs.hwids = [the_id for _ in range(0, len(cmdArgs.paths))]

    funcs = fileUtility.parse_func_specs(cmdArgs.spec)  # parse func specs

    # modify sys path to include relevant files
    for path in cmdArgs.paths:
        sys.path.append(path)
    sys.path.append(dirname(cmdArgs.sol))
    cmdArgs.sol = basename(cmdArgs.sol)[:-3]

    for path, hwid in zip(cmdArgs.paths, cmdArgs.hwids):
        section = fileUtility.read_folder(path)
        section.grade_section(cmdArgs.sol, funcs)
        section.write_test_results(cmdArgs.out_dir)
        section.write_grade_sheet(cmdArgs.out_dir, hwid)

    print('Grading Finished')


if __name__ == '__main__':
    main()
