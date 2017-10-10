#works with python 3.5 and windows. not tested with 3.6 or mac/linux
##Willem DeJong##

import solution_file as D#a file you write that does the things that the student's code should do. this method only works with purely deterministic functions. any functions that can have different outputs for a given output should be handle by checking that the outputs conforms the problem (the hard part here is making sure their scope isn't too narrow like if the function is supposed to return a RN between 1 and 10 and they do only RN between 4-7.)
import random
import os
import sys
    
def teste(stfile,path="",err=open("error.txt","w")):
    #stfile is the name of the file (ex. "studentA_HW1")
    #path is the path of the containing folder of the student's .py file
    #err is created by the readclass.py file and is just a class wide error log.
    if path!="":#if a path is given it adds it to the local list of paths so that the file can be found by the __import__ function. I found that __import__ didn't work with a full path. nor does it work when the .py extention was included
        sys.path.insert(0,path)
    stf=__import__(stfile)
    #g is the returned list. the first thing in g should be the list of hawkIDs if the students write this function wrong they will not automatically get a grade. When you notice someone turned in a file but didn't receive a score you can find check the csv with the same name as the assignment column header in the same location as readclass.py to see grades by file. in this case if you are giving credit for the getHawkID function subtact it from that score
    g=[stf.getHawkIDs(),0]#this 1 is giving credit for the getHawkIDs
    berrs=str(g[0])+"\n"#berrs is used to construct the resulting score to be written to the students file 
    errs=""#errs is for constructing an error log. I did this to record on students .py file when the result of their function didn't match the expected result.
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
    err.write(errs)
    err2=open(path+"/"+stfile+"_errors.txt","w")
    err2.write(errs)
    err2.close()
    try:
        err3=open(path+"/"+stfile+".py","r")
        pyfi=err3.read()
        err3.close()
        iii=pyfi.find("#"+stfile+"_errors.txt")
        if iii==-1:
            iii=len(pyfi)
        try:
            err3=open(path+"/"+stfile+".py","w")
            err3.write(pyfi[0:iii]+"\n\n#"+stfile+"_errors.txt\n")
            lines=errs.split("\n")
            for line in lines:
                err3.write("#"+line+"\n")
            err3.close()
        except:
            err3.close()
    except:
        pass
    return g
