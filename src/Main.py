""" entry point of grading script """

import File_Utility
import argparse
import sys
from os.path import dirname
from os.path import basename

# help strings for command line arguments
P_HELP = 'Paths to folders representing all submitted files of each section. Each folder should directly contain all ' \
         '.py files submitted by stuents and only 1 csv file that is the grade sheet of that section downloaded from ' \
         'ICON'
I_HELP = 'Homework IDs (column header of the homework entry in the grade sheet). They should be entered in the same ' \
         'order with sections provided in -P arguments'
S_HELP = 'Path to solution file'
F_HELP = 'Path to function spec file. See \"example\" folder at https://github.com/r2dong/Intro-to-CS-Grading-Script ' \
         'for an example'
O_HELP = 'Path to output folder. Any comments and grade sheet will be created as copies, and the original files will ' \
         'not be affected'


def main():
    """ entry point of grading script """

    parser = argparse.ArgumentParser()  # parse command line arguments
    parser.add_argument('-p', nargs='+', dest='paths', type=str, required=True, help=P_HELP)
    parser.add_argument('-i', nargs='+', dest='hwids', type=str, required=True, help=I_HELP)
    parser.add_argument('-s', dest='sol', type=str, required=True, help=S_HELP)
    parser.add_argument('-f', dest='spec', type=str, required=True, help=F_HELP)
    parser.add_argument('-o', dest='out_dir', type=str, required=True, help=O_HELP)
    args = parser.parse_args()

    if len(args.hwids) != 1 and len(args.hwids) != len(args.paths):
        raise Exception('invalid section folder and hwid input')
    if len(args.hwids) == 1:
        the_id = args.hwids[0]
        args.hwids = [the_id for _ in range(0, len(args.paths))]

    funcs = File_Utility.parse_func_specs(args.spec)  # parse func specs

    # modify sys path to include relevant files
    for path in args.paths:
        sys.path.append(path)
    sys.path.append(dirname(args.sol))
    args.sol = basename(args.sol)[:-3]

    for path, hwid in zip(args.paths, args.hwids):
        section = File_Utility.read_folder(path)
        section.grade_section(args.sol, funcs)
        section.write_test_results(args.out_dir)
        section.write_grade_sheet(args.out_dir, hwid)

    print('Grading Finished')


if __name__ == '__main__':
    main()
