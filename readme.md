Python Unit Testing (Developing)
===================

### Overview
Correctness of functions are determined by comparing return value with either a correct implementation or a set of hard-coded inputs and return values. This program works only for pure functions (those return fixed values given fixed input). Test results are appended to source files being tested, and additional instructions may be provided for more customized output.

If a correct implementation is available, all input parameters of a function are specified, and the program generates according random values as inputs. It then checks if the function being tested and the correct implementation share the same return value.

A GUI is being developed currently, and a more detailed description on usage will be provided once everything is integrated and packaged.

### Motivation
Previously a script was developed for grading homework for a introductory level python course. The script hard-coded function calls to both submissions and the solution, as well as writting output to submission source files. As a result, the script needs to be re-written for each homework, which was error-prone and time-consuming: for exmaple, it is very easy to mess up building the strings to be re-written, and submitted files sometime modify input through references, in which case the script mistakenly marks points off the submission. 
