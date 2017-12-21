# This script was originally written by Willem Dejong. Rentian worked on
# improving style of the code and making a few improvements to functionality.

# Development Notes
# Correct Scores should be [[['jaalbaugh'], 0, 1, 0, 0, 1], [['ljcochrane'], 0, 1, 1, 1, 1]], and
# [[['edbuckley'], 0, 1, 1, 1, 1], [['tntrres'], 0, '0', '0', '0', '0']]

#to record name
import os
import re
import tester

#

#reads in the list of file/folders in path and make a list of .py files 
def readFolder(path):
    #creates a list of items in the directory of path
    fileList=os.listdir(path)
    
    #removes testing .py codes from fileList, if they are in it
    if "tester.py" in fileList:
        fileList.remove("tester.py")
    if "readclass.py" in fileList:
        fileList.remove("readclass.py")
    if "solution.py" in fileList:
        fileList.remove("solution.py")

    # remove all none py file names from fileList
    index = 0 # loop index 
    while index < len(fileList):
        # finds index of last '.' in file names. If no '.', it will be 0 and 
        # will check against the entire file name and fail. (unlesss it is a
        # folder named "py", so don't name a folder "py" in this directory.)
        try:
            fileExtIndex = fileList[index].rfind(".") + 1
        except:
            break
        #if it does not have a "py" as a the file extention remove from list
        if fileExtIndex == -1 or fileList[index][fileExtIndex:].lower() != "py":
            try:
                fileList.remove(fileList[index])
            except:
                print("Failed removing non-py file")
        else:
            index += 1
    
    # make all file names absolute paths
    absoluteFileList = []
    for fileName in fileList:
        absoluteFileList.append(fileName)
        
    #returns fileList containing only names of .py files
    return fileList

# find and return the column number of a sepcific header, among a row of
# headers delimited by commas
# Input:
# header - the header line from the ICON exported csv
# hwid - the header 
# Output:
# an integer >= 0 representing the column number
def findColumn(headerRow, header):
    
    colNum = -1 # column number of header
    start = 0 # starting index of header to look for in string
    
    while True:
        end = headerRow.find(",", start) # index of the next comma
        if end == -1:
            return colNum + 1
        if headerRow[start:end] == header:
            break
        start = end + 1
        colNum += 1
    return colNum + 1 # colNum returned will be at least 0

# "insert" score of students into csv to be uploaded
def insertScore(Stng, Identifier, numcomma, score):
    if type(Identifier)!=str:
        return Stng
    try:
        if type(int(Identifier))==int:
            print("X")
            return Stng
    except:
        pass
    ind=Stng.find(","+Identifier+",")+1
    print(ind)
    iii=Stng.rfind(",",0,ind-1)+1
    print(iii)
    print(Stng[iii:ind-1])
    try:
        int(Stng[iii:ind-1])
    except:
        print("XX")
        return Stng
    if ind==0:
        print("XXX")
        return Stng
    for i in range(0,numcomma):
        ind=Stng.find(",",ind)+1
    if ind==0:
        return Stng
    ind2=Stng.find(",",ind)
    if ind2==-1:
        return Stng[:ind]+str(score)
    else:
        return Stng[:ind]+str(score)+Stng[ind2:]

# removes extra columns from CSV to re-import to ICON, so that empty spaces do
# not overwrite other grades
def removeExtraCol(outfile,hwid):
    f=open(outfile,"r")
    nf=""
    b=True
    colHwid=0
    for line in f:
        if b:
            colHwid=findColumn(line,hwid)
            colHwid-=4
            b=False
        ind=-1
        for i in range(0,4): # changed from 5 to 4 Aug 23 2017
            ind=line.find(",",ind+1)
        
        nf=nf+line[:ind]
        ind2=ind
        for i in range(0,colHwid):
            ind2=line.find(",",ind2+1)
        #print(line[ind2:line.find(",",ind2+1)])
        #input()
        nf=nf+line[ind2:line.find(",",ind2+1)]+"\n"
        #1print(nf)
    #pyfi=f.read()
    f.close()
    #print(nf)
    f=open(outfile,"w")
    f.write(nf)
    f.close()
    
# stfResults is returned by Main.testFile
# writes at the end of the file
def writeComments(stfResults):
    
    for result in stfResults:
        absolutePath = result.path + result.name
        stf = open(absolutePath, "r")
        contents = stf.read()
        stf.close()
        
        comments = str(result)
        comments = toggleComment(comments)
        stf = open(absolutePath, "w")
        stf.write(contents + "\n" + comments)
        stf.close()

# add "#" to each line of comment
def toggleComment(comment):
    comment = "# " + comment
    comment = comment.replace("\n", "\n# ")
    return comment

# remove the extension from a string file name
def removeExtension(fileName):
    extLoc = fileName.rfind(".")
    if extLoc == -1:
        # do nothing if file name has no extension
        return fileName
    else:
        return fileName[:extLoc]
    
