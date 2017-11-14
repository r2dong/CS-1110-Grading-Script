# This tester works with only purely deterministic functions, i.e, functions
# that guarantes to yield identical output with identical input. For
# undeterministic functions, such as ones involving random numbers, it is
# recommended to visually inspect the printed output of the function.

# Works with python 3.6 and windows, and not yet tested on Linux.
##Willem DeJong##

import solution_file as D#
import random
import os
import sys

# test output of functions of a studnet against a solution file
# Input: 
# stuFile - name of student's file, without .py suffix
# path - path to foler containing stuFile
def teste(stuFile, path=""):
    # if path given, adds it to local paths so that the file can be found by 
    # __import__ function. (_import_ work with neither full path nor when .py
    # included
    if path!="":
        sys.path.insert(0,path)
    stf=__import__(stuFile)
    # g is a list to record grades, first element of g is the list of hawkIDs.
    g=[stf.getHawkIDs(),0]#this 1 is giving credit for the getHawkIDs
    berrs=str(g[0])+"\n"# resulting score to write into student's file 
    errs="" # log differences between expected output and actual output
    n=""
    #***************************************************************************
    # test getMidpoint()
    try:
        point = 1 #assign point value
        errs = errs + "getMidpoint\n" # this labels in the error log the start of testing said function
        
        # generate the test cases
        x1 = [];
        y1 = [];
        x2 = [];
        y2 = [];
        for index in range(0, 4):
            x1.append((random.random() - 0.5) * 50)
            y1.append((random.random() - 0.5) * 50)
            x2.append((random.random() - 0.5) * 50)
            y2.append((random.random() - 0.5) * 50)
        
        # run through all testcases
        for i in range(0, len(x1)):
            
            #call the function for both the solution and the student's code
            a = D.getMidpoint(x1[i], y1[i], x2[i], y2[i])
            b = stf.getMidpoint(x1[i], y1[i], x2[i], y2[i])
            
            if a != b:#compare result
                errs=errs+"<pb1>"#tag that is use to clean the class wide errorlog. the tag should be <pb#> where # is the problem number with respect to how many problems there are. if the getHawkIDs function is given credit it counts as 1.
                #errs=errs+"\nin: "+str(
                
    
                errs=errs+"\ncorrect-out:"
                if type(a)==str:
                    errs=errs+"\""+a+"\""
                else:
                    errs=errs+str(a)
                errs=errs+"\n actual-out:"
                if type(b)==str:
                    errs=errs+"\""+b+"\""
                else:
                    errs=errs+str(b)
                errs=errs+"\n</pb1>\n"
                point=0
                
        if point==1:
            errs=errs+"all good\n"
        
        errs=errs+"\n"
        g.append(point)
        
    except:
        errs=errs+"\nruntime error\n\n"
        g.append("0")
        
    #***************************************************************************
    # test getAverage()
    try:
        point = 1
        errs=errs+"getAverage\n"
        
        x = [];
        y = [];
        c = [];
        d = [];
        e = [];
    
        for index in range(0, 5):
            x.append((random.random() - 0.5) * 100)
            y.append((random.random() - 0.5) * 100)
            c.append((random.random() - 0.5) * 100)
            d.append((random.random() - 0.5) * 100)
            e.append((random.random() - 0.5) * 100)
            
        for i in range(0, len(x)):
            a = D.getAverage(x[i], y[i], c[i], d[i], e[i])
            b = stf.getAverage(x[i], y[i], c[i], d[i], e[i])
                
            if a != b:
                errs=errs+"<pb2>"
                errs=errs+"\ncorrect-out:"
                if type(a)==str:
                    errs=errs+"\""+a+"\""
                else:
                    errs=errs+str(a)
                errs=errs+"\n actual-out:"
                if type(b)==str:
                    errs=errs+"\""+b+"\""
                else:
                    errs=errs+str(b)
                errs=errs+"\n</pb2>\n"
                point=0
                
        if point==1:
            errs=errs+"all good\n"
            
        errs=errs+"\n"
        g.append(point)

    except:
        errs=errs+"\nruntime error\n\n"
        g.append("0")
    
    #***************************************************************************
    # test getAverageString()
    try:
        point = 1
        errs = errs + "getAverageString\n"
        
        # using test cases from the previous problem
        for i in range(0, len(x)):
            a = D.getAverageString(x[i], y[i], c[i], d[i], e[i])
            b = stf.getAverageString(x[i], y[i], c[i], d[i], e[i])
            
            if a != b:
                errs=errs+"<pb3>"
                errs=errs+"\ncorrect-out:"
                if type(a)==str:
                    errs=errs+"\""+a+"\""
                else:
                    errs=errs+str(a)
                errs=errs+"\n actual-out:"
                if type(b)==str:
                    errs=errs+"\""+b+"\""
                else:
                    errs=errs+str(b)
                errs=errs+"\n</pb3>\n"
                point=0
                
        if point==1:
            errs=errs+"all good\n"
            
        errs=errs+"\n"
        g.append(point)

    except:
        errs=errs+"\nruntime error\n\n"
        g.append("0")    
    
    #***************************************************************************
    # test getLength
    try:
        point = 1
        errs = errs+"getLength\n"
        
        x1 = 1.5
        x2 = 2.2
        
        a = D.getLength(x1, x2, "H")
        b = stf.getLength(x1, x2, "H")
        
        if a!=b:
            errs=errs+"<pb4>"
            errs=errs+"\ncorrect-out:"
            if type(a)==str:
                errs=errs+"\""+a+"\""
            else:
                errs=errs+str(a)
            errs=errs+"\n actual-out:"
            if type(b)==str:
                errs=errs+"\""+b+"\""
            else:
                errs=errs+str(b)
            errs=errs+"\n</pb4>\n"
            point=0
        
        #----
        
        a = D.getLength(x1, x2, "S")
        b = stf.getLength(x1, x2, "S")
        
        if a!=b:
            errs=errs+"<pb4>"
            errs=errs+"\ncorrect-out:"
            if type(a)==str:
                errs=errs+"\""+a+"\""
            else:
                errs=errs+str(a)
            errs=errs+"\n actual-out:"
            if type(b)==str:
                errs=errs+"\""+b+"\""
            else:
                errs=errs+str(b)
            errs=errs+"\n</pb4>\n"
            point=0
        
        # -------
        a = D.getLength(x2, x1, "S")
        b = stf.getLength(x2, x1, "S")
        
        if a!=b:
            errs=errs+"<pb4>"
            errs=errs+"\ncorrect-out:"
            if type(a)==str:
                errs=errs+"\""+a+"\""
            else:
                errs=errs+str(a)
            errs=errs+"\n actual-out:"
            if type(b)==str:
                errs=errs+"\""+b+"\""
            else:
                errs=errs+str(b)
            errs=errs+"\n</pb4>\n"
            point=0        
                
        if point==1:
            errs=errs+"all good\n"
            
        errs=errs+"\n"
        g.append(point)
        
    except:
        errs=errs+"\nruntime error\n\n"
        g.append("0")   
    
    #---------------------------------------------------------------------------    
#a log looks like this 

#funcName1
#<pb2>
#correct-out: xxxxxxxxxxxx
# actual-out: yyyyyyyyyyyy
#</pb2>
#<pb2>
#correct-out: xxxxxxxxxxxx
# actual-out: yyyyyyyyyyyy
#</pb2>
    #*****************logs student's errors***********************************
    berrs=berrs+"Scores:\n"
    x=1
    for i in g[1:]:
        berrs+="\t"+str(x)+") "+str(i)+"\n"
        x+=1
    errs=berrs+"\n"+errs
    err2=open(path+"/"+stuFile+"_errors.txt","w")
    err2.write(errs)
    err2.close()
    try:
        err3=open(path+"/"+stuFile+".py","r")
        pyfi=err3.read()
        err3.close()
        iii=pyfi.find("#"+stuFile+"_errors.txt")
        if iii==-1:
            iii=len(pyfi)
        try:
            err3=open(path+"/"+stuFile+".py","w")
            err3.write(pyfi[0:iii]+"\n\n#"+stuFile+"_errors.txt\n")
            lines=errs.split("\n")
            for line in lines:
                err3.write("#"+line+"\n")
            err3.close()
        except:
            err3.close()
    except:
        pass
    return g
