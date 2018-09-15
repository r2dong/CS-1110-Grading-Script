Grading Script for UIowa CS:1110 Introduction to CS
===================

Grading is done by comparing return values of functions submitted by students and that of
a solution function. We assume these functions to be fully determinstic, such that there is a
one-to-one relationship between input arguments and return values.

## Usage
<pre>
usage: Main.py [-h] -p PATHS [PATHS ...] -i HWIDS [HWIDS ...] -s SOL -f SPEC
               -o OUT_DIR

optional arguments:
  -h, --help            show this help message and exit
  -p PATHS [PATHS ...]  Paths to folders representing all submitted files of
                        each section. Each folder should directly contain all
                        .py files submitted by stuents and only 1 csv file
                        that is the grade sheet of that section downloaded
                        from ICON
  -i HWIDS [HWIDS ...]  Homework IDs (column header of the homework entry in
                        the grade sheet). They should be entered in the same
                        order with sections provided in -P arguments
  -s SOL                Path to solution file
  -f SPEC               Path to function spec file. See "example" folder at
                        https://github.com/r2dong/Intro-to-CS-Grading-Script
                        for an example
  -o OUT_DIR            Path to output folder. Any comments and grade sheet
                        will be created as copies, and the original files will
                        not be affected
</pre>

## Edge Cases Handled
- incorrect hawk id: comments will still be provided, but the student recieve 0 for the assignment
- syntax errors in submissions: 0 assigned for the submission
- infinte loops: given complexity of assignments, it is assumed that execution of any function would be < 5 sec.
0 is assigned for the function with infinite loops
- incorrect function names/(basically when the function could not be found): 0 is assigned for the function 
- incorrect function signature (i.e., incorrect number of input args): same as runtime error
- runtime errors: 0 is assigned for the function

## Example
All sample files necessary to conduct one grading are in the example/ folder, and corresponding outputs are in <br>
example/Grading_Output/. The command line arugments required are in arguments.txt.