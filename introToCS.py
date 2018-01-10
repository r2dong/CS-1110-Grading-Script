from fileUtility import *

stuInfoColNum = 3 # largest column number containing student info on the left
insertCol = stuInfoColNum + 1 # colum number to write student scores
IDCol = 2 

def writeOutput(stfResults, optArgs):
    
    outFileName = optArgs[0] # consider removing, user really need no control over this
    hwID = optArgs[1]
    fullCSVName = optArgs[2]
    
    fullMatrix = csvToMatrix(fullCSVName)
    matrix = removeExtraCol(fullMatrix, hwID)
    
    for result in stfResults:
        
        # get the hawkIDs
        curFile = __import__(removeExtension(result.name))
        try:
            hawkIDs = curFile.getHawkIDs()
            print("hawkIDs retrieved: " + str(hawkIDs), flush = True)
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
    
    
        