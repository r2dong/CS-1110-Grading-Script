from fileUtility import *

stuInfoColNum = 3  # largest column number containing student info from the left
insertCol = stuInfoColNum + 1  # colum number to write student scores
IDCol = 2  # column number where hawkID is in
numArg = 3  # number of arguments needed for writeSectionOutput


# writes csvs for all sections to re-upload to ICON
# Inputs:
# stfResults - <[[studentFile]]> litst of student files collected in an outer
#              list, ordered by sections
# optArgs - <[[str, str, str]]> inside tuple, elements are
#           respectively name of output file, hwID, and file name of csv
#           downloaded from ICON. Follows same order as stfResults
def writeOutput(stfResults, optArgs):
    # if len(stfResults) != len(optArgs):
    #     raise Exception("Error in section information")
    # else:
    #     optArgs = cmdArgToInput(optArgs)
    #     for result, arg in zip(stfResults, optArgs):
    #         writeSectionOutput(result, arg)
    # optArgs = cmdArgToInput(optArgs)
    for result in stfResults:
        writeSectionOutput(result, optArgs)


# writes a csv to re-upload to ICON for one section
def writeSectionOutput(stfResults, optArgs):
    outFileName = optArgs[0]  # consider removing, user really need no control over this
    hwID = optArgs[1]
    fullCSVName = optArgs[2]

    fullMatrix = csvToMatrix(fullCSVName)
    matrix = removeExtraCol(fullMatrix, hwID)

    for result in stfResults:

        # get the hawkIDs
        curFile = __import__(removeExtension(result.name))
        try:
            hawkIDs = curFile.getHawkIDs()
            print("hawkIDs retrieved: " + str(hawkIDs), flush=True)
        except:
            # skip file if getHawkID function is wrong
            continue

        # get total score
        total = 0
        funcs = result.funcs
        for func in funcs:
            point = func.score
            funcResults = func.testResults
            for funcResult in funcResults:
                if not funcResult.isCorrect:
                    point = 0
                    break
            total += point

        for ID in hawkIDs:
            writeScore(total, ID, matrix)

    matrixToCsv(matrix, outFileName)


# remove non-used columns in the grade sheet
def removeExtraCol(matrix, colHeader):
    newMatrix = []
    colToKeep = findColumn(matrix, colHeader)
    for row in matrix:
        col = 0
        newRow = []
        for element in row:
            if col <= stuInfoColNum or col == colToKeep:
                newRow.append(element)
            col += 1
        newMatrix.append(newRow)
    return newMatrix


# write score to corresponding ID
def writeScore(point, ID, matrix):
    for row in matrix:
        if row[IDCol] == ID:
            row[insertCol] = point
            break


# convert arguments from cmdLine format to that needed by writeOutput
# Inputs:
# cmdArgs - <[str]> raw command line arguments recieved
# def cmdArgToInput(cmdArgs):
#     if len(cmdArgs) % numArg != 0:
#         errMsg = "Incorrect number of inputs to IntroToCS writeOutput"
#         raise Exception(errMsg)
#     else:
#         formattedArgs = []
#         for index in range(0, len(cmdArgs) / numArg):
#             sectionArgList = []
#             for argIndex in range(0, numArg):
#                 sectionArgList.append(cmdArgs[index + argIndex])
#             formattedArgs.append(sectionArgList)
#         return formattedArgs
