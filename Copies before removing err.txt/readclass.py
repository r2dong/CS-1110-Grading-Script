###Willem DeJong###

#to record name
import os
import re
import tester

#**********************************************************************************************************************************
#These are to be changed as needed

# list containing integers representing the section(s) to skip
skipsections=[1, 2, 3, 4, 5]

#PATH is the path to the folder containing all the .py files
PATH1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/file"
PATH2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/file"
PATH3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/file"
PATH4="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/4/file"
PATH5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/file"
PATH6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6"
PATH7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7"

# number of problem for this assignment
NUMPROB = 4

# HWID is the string that matches exactly the header of the column that you are adding scores to in the icon exported csv
HWID1="DA 2 Final Submission (540834)"
HWID2="DA 2 Final Submission (547156)"
HWID3="DA 2 Final Submission (547323)"
HWID4="DA 2 Final Submission (548734)"
HWID5="DA 2 Final Submission (549085)"
HWID6="DA 2 Final Submission (548736)"
HWID7="DA 2 Final Submission (548738)"

#INFILE is the path to the icon exported csv that you are reading from
INFILE1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/05_Sep_20_20_Grades-CS_1110_0A01_Fall17.csv"
INFILE2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/05_Sep_20_24_Grades-CS_1110_0A02_Fall17.csv"
INFILE3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/05_Sep_20_26_Grades-CS_1110_0A03_Fall17.csv"
INFILE4="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/4/05_Sep_20_27_Grades-CS_1110_0A04_Fall17.csv"
INFILE5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/05_Sep_20_28_Grades-CS_1110_0A05_Fall17.csv"
INFILE6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6/05_Sep_20_29_Grades-CS_1110_0A06_Fall17.csv"
INFILE7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7/05_Sep_20_31_Grades-CS_1110_0A07_Fall17.csv"

#OUTFILE is the path to the csv file you wish to create/overwrite with the INFILE + added scores
OUTFILE1="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/1/newGrades1.csv"
OUTFILE2="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/2/newGrades2.csv"
OUTFILE3="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/3/newGrades3.csv"
OUTFILE4="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/4/newGrades4.csv"
OUTFILE5="C:/Users/Rentian Dong/Desktop/CS 1110/Week 2/AutoGrading/submissions/5/newGrades5.csv"
OUTFILE6="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/6/newGrades6.csv"
OUTFILE7="C:/Users/Rentian Dong/Desktop/CS 1110/Improving Grading Script/7/newGrades7.csv"

# true if you want write grade after each file check
inTimeWrite=True
#**********************************************************************************************************************************

#reads in the list of file/folders in path then uses that to make a list of .py files 
def readfolder(path):
    #creates a list of items in the directory of path
    fileList=os.listdir(path)
    
    #removes testing .py codes from fileList
    try:
        fileList.remove("tester.py")
    except:
        print("Unable to find test function")
    try:
        fileList.remove("readclass.py")
    except:
        print("Unable to find readClass function")

    # remove all none py file names from fileList
    index = 0 # loop index
    # contents of fileList modified during 
    while index < len(fileList):
        #finds index of last '.' if no '.' it will be 0 and will check against full string and fail. (unlesss it is a folder named "py".... don't name a folder "py" in this directory.)
        try:
            fileExtIndex = fileList[index].rfind(".") + 1 # index of "." for file extensions
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
    
    #returns fileList containing only names of .py files
    return fileList


#will need to modify later to account for possible infinite loops
# Inputs:
# pyFileList - a list with python file names to be graded
# hwid - header of column grades should be written to from ICON exported .csv
# infile - path to icon exported csv
# outfile - path to .csv file to write new grades to
# path - path to folder with all python files to be graded
# err - 
# 
# Output:
# a variable named "glist"
def runtester(pyFileList, hwid, infile, outfile, path, err):
    
    csvIcon = open(infile, "r") # open original ICON csv file read-only
    # create new csv file to record grades, this file is not the one uploaded to
    # ICON at the end, looks like is only for double checking grades
    # csvNew = open(hwid + ".csv", "w") 
    pyfi = ""
    
    # extract line with all headers from ICON csv
    for line in csvIcon: # type of line is string
        header = line.replace("\n","")
        break
    csvIcon.close()
    
    colHwid = findColumn(header, hwid) # column number in header of hwid
    colHwid = colHwid - 2
    
    csvIcon=open(infile,"r")
    pyfi=csvIcon.read()
    csvIcon.close()
    #creates empty glist for grades it will be a list of lists the first internal list will be the list of hawkid(s), the rest of the internal lists will be the points for each problem. 1 for correct function, 0 for incorrect function and the string "0" if an error is raised in calling it.
    glist=[]
    #loop that goes through pyFileList
    for i in range(0,len(pyFileList)):
        #trys to run the tester. if tester.py fails to load the grade element apended to the grade list will be -1
        print("starting: "+pyFileList[i][:pyFileList[i].rfind(".py")])
        try:
            #cuts off the .py from each name and passes it into teste the results of which are appended to glist
            err.write(pyFileList[i][:pyFileList[i].rfind(".py")]+"\n")
            glist.append(tester.teste(pyFileList[i][:pyFileList[i].rfind(".py")],path,err))
            err.write("****************************************************************\n\n")
        except:
            err.write("****************************************************************\n\n")
            #if failed to load
            glist.append(-1)
        if inTimeWrite:
            if glist[i]!=-1:
                sum=0
                for ele in glist[i]:
                    if type(ele)!=list:
                        try:
                            sum+=int(ele)
                        except:
                            pass
                if type(glist[i][0])==list or glist[i][0]==tuple:
                    for elele in glist[i][0]:
                        pyfi=insertScore(pyfi,elele.lower(),colHwid,sum)
                        csvIcon=open(outfile,"w")
                        csvIcon.write(pyfi)
                        csvIcon.close()
        try:    
            f=open(path+"/"+pyFileList[i],"r")
            pyf=f.read()
            f.close()
            f=open(path+"/"+pyFileList[i],"w")
            f.write("#$$##Grades:"+str(glist[i])+"\n"+pyf)
            f.close()
        except:
            pass
    print(glist)
    return glist

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

def insertScore(Stng,Identifier,numcomma,score):
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
    
    
def writeclass(clist,glist,hwid,infile,outfile):
    f2=open(infile,"r")
    header=""
    for l in f2:
        header=l.replace("\n","")
        break
    f2.close()
    colHwid=findColumn(header,hwid)
    print(colHwid)
    colHwid=colHwid-2
    f2=open(infile,"r")
    pyfi=f2.read()
    f2.close()
    f2=open(hwid+".csv","w")
    f2.write("name,")
    for i in range(1,NUMPROB+1):
        f2.write(str(i)+",")
    f2.write("total\n")
    index=0
    for ele in glist:
        f2.write(clist[index]+",")
        if ele!=-1:
            if type(ele[0])==list:
                sislist=ele.pop(0)
            sum=0
            for i in ele:
                f2.write(str(i)+",")
                sum=sum+int(i)
            f2.write(str(sum))
            if type(ele[0])==list:
                for ele2 in sislist:
                    pyfi=insertScore(pyfi,ele2.lower(),colHwid,sum)
        f2.write("\n")
        index+=1
    f2.close()
    f2=open(outfile,"w")
    f2.write(pyfi)
    f2.close()

def removeExtraCol(outfile,hwid):
    f=open(outfile,"r")
    nf=""
    b=True
    colHwid=0
    for line in f:
        if b:
            colHwid=findColumn(line,hwid)
            colHwid-=4
            #print(colHwid)
            #input()
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
def uniqeErr(numprob):
    err=open("error.txt","r")
    errs=err.read()
    err.close()
    nerrs=""
    for p in range(1,numprob+1):
        errs2=""
        tag="pb"+str(p)
        errs2=errs2+tag+"\n"
        stag="<"+tag+">"
        istag=len(stag)
        etag="</"+tag+">"
        ietag=len(etag)
        i=errs.find(stag)
        ii=errs.find(etag)
        tem=[]
        while i!=-1:
            errlog=errs[i+istag+1:ii]
            if errlog not in tem:
                tem.append(errlog)
                errs2=errs2+errlog
            i=errs.find(stag,ii)
            ii=errs.find(etag,i)
        nerrs=nerrs+"\n"+errs2
    err2=open("unique_errors.txt","w")
    err2.write(nerrs)
    err2.close()
    
# main function
err=open("error.txt","w")
if 1 not in skipsections:
    clist=readfolder(PATH1) # list of py files in the directory
    glist=runtester(clist,HWID1,INFILE1,OUTFILE1,PATH1,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID1,INFILE1,OUTFILE1)
    removeExtraCol(OUTFILE1,HWID1)
if 2 not in skipsections:
    clist=readfolder(PATH2)
    glist=runtester(clist,HWID2,INFILE2,OUTFILE2,PATH2,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID2,NUMPROB,INFILE2,OUTFILE2)
    removeExtraCol(OUTFILE2,HWID2)
if 3 not in skipsections:
    clist=readfolder(PATH3)
    glist=runtester(clist,HWID3,INFILE3,OUTFILE3,PATH3,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID3,NUMPROB,INFILE3,OUTFILE3)
    removeExtraCol(OUTFILE3,HWID3)
if 4 not in skipsections:
    clist=readfolder(PATH4)
    print(clist)
    glist=runtester(clist,HWID4,INFILE4,OUTFILE4,PATH4,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID4,NUMPROB,INFILE4,OUTFILE4)
    removeExtraCol(OUTFILE4,HWID4)
if 5 not in skipsections:
    clist=readfolder(PATH5)
    glist=runtester(clist,HWID5,INFILE5,OUTFILE5,PATH5,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID5,NUMPROB,INFILE5,OUTFILE5)
    removeExtraCol(OUTFILE5,HWID5)
if 6 not in skipsections:
    clist=readfolder(PATH6)
    glist=runtester(clist,HWID6,INFILE6,OUTFILE6,PATH6,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID6,NUMPROB,INFILE6,OUTFILE6)
    removeExtraCol(OUTFILE6,HWID6)
if 7 not in skipsections:
    clist=readfolder(PATH7)
    glist=runtester(clist,HWID7,INFILE7,OUTFILE7,PATH7,err)
    if not inTimeWrite:
        writeclass(clist,glist,HWID7,NUMPROB,INFILE7,OUTFILE7)
    removeExtraCol(OUTFILE7,HWID7)
err.close()
uniqeErr(NUMPROB)