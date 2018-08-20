import fileUtility
import argparse
import sys
from os.path import dirname
from os.path import basename
from Newtester import grade_files


def main():

    parser = argparse.ArgumentParser()  # parse command line arguments
    parser.add_argument("-p", nargs="+", dest="paths", type=str)  # section folders
    parser.add_argument("-s", dest="sol", type=str)  # solution file path
    parser.add_argument("-f", dest="spec", type=str)  # function spec file path
    cmdArgs = parser.parse_args()

    funcs = fileUtility.parse_func_specs(cmdArgs.spec)  # parse func specs

    # modify sys path to include relevant files
    for path in cmdArgs.paths:
        sys.path.append(path)
    sys.path.append(dirname(cmdArgs.sol))

    no_ext_sol_name = basename(cmdArgs.sol)[:-3]
    sections = grade_files(cmdArgs.paths, no_ext_sol_name, funcs)  # run all tests
    for section in sections:
        section.write_feedback()
    print(1)


if __name__ == '__main__':
    main()
