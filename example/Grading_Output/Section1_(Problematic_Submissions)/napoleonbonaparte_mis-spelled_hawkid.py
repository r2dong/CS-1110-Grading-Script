#Problem 1: Write a function that takes no arguments and returns a list containing your
#HawkID.
def getHawkIDs():
    return ["nbona, but I am so handsome and smart"]

#DA 2 get cordinates of 2 points and find the midpoint
def getMidpoint(x1, y1, x2, y2):
    #get average of Xs
    xAve= (x1+x2)/2
    #round to the nearest tenth
    xAve= round(xAve, 1)
    #get ave of Ys
    yAve= (y1+y2)/2
    #ditto
    yAve= round(yAve, 1)
    #return a lost with the averages
    myList=[xAve,yAve]
    return myList

#DA 3 make a function that gets the average of 5 numbers and rounds to the nearest tenth
def getAverage(p1,p2,p3,p4,p5):
    #make a variable that keeps track of the sum of all the numbers
    mySum = p1+p2+p3+p4+p5
    #make a variable that gets and holds the average
    myAve = mySum/5
    #round to the nearest tenth
    round(myAve, 1)
    #return ave
    return myAve

#DA 4 similar to DA3 get average of 5 numbers. return a string instead of a number
def getAverageString(p1,p2,p3,p4,p5):
    #make a variable that keeps track of the sum of all the numbers
    mySum = p1+p2+p3+p4+p5
    #make a variable that gets and holds the average
    myAve = mySum/5
    #round to the nearest tenth
    round(myAve, 1)
    #make a string saying the average
    myString = ("The average value is "+str(myAve)+".")
    #return myString
    return myString

#DA5
def getLength(p1,p2, myString):
    #Need to declare 3 variables to use for later. One to keep track of myLenth
    #and 2 to move my entered variables to see witch one is larer
    myLength = 0
    h=0
    s=0
    #I have 2 if statements to see witch string was taken as an argument
    if myString==str("H"):
        #calculate
        myLength=((p1**2)+(p2**2))**.5
    if myString==str("S"):
        if p1>p2:
            h=p1
            s=p2
        else:
            h=p2
            s=p1
        myLength = ((h**2)-(s**2))**.5
        #round my length to the nearest tenth
    myLength = round(myLength,1)
    return myLength




# ###############function: getHawkIDs, score: 0/1###############
# could not find a match for the hawk id you returned in getHawkIDs function
# maybe you did not spell it right?
# Note that you are assigned a score of 0 for this
# Please discuss with a TA ASAP IN PERSON to recieve credit for this assignment
# 
# ############### function: getMidpoint, score: 1/1###############
# 1 cases were tested
# case 0
# inputs: (1, 5, 9, 13)
# +----------+----------------+----------------+
# | PASSED   | value returned | type returned  |
# +----------+----------------+----------------+
# | expected | [5.0, 9.0]     | <class 'list'> |
# +----------+----------------+----------------+
# | actual   | [5.0, 9.0]     | <class 'list'> |
# +----------+----------------+----------------+
# 
# 
# ############### function: getAverage, score: 1/1###############
# 3 cases were tested
# case 0
# inputs: (1, 2, 3, 4, 5)
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 3.0            | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 3.0            | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# case 1
# inputs: (2, 4, 6, 8, 10)
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 6.0            | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 6.0            | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# case 2
# inputs: (-1, -2, 0, 2, 1)
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 0.0            | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 0.0            | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# ############### function: getAverageString, score: 1/1###############
# 3 cases were tested
# case 0
# inputs: (1, 2, 3, 4, 5)
# +----------+-----------------------------+---------------+
# | PASSED   | value returned              | type returned |
# +----------+-----------------------------+---------------+
# | expected | "The average value is 3.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# | actual   | "The average value is 3.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# 
# 
# case 1
# inputs: (2, 4, 6, 8, 10)
# +----------+-----------------------------+---------------+
# | PASSED   | value returned              | type returned |
# +----------+-----------------------------+---------------+
# | expected | "The average value is 6.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# | actual   | "The average value is 6.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# 
# 
# case 2
# inputs: (-1, -2, 0, 2, 1)
# +----------+-----------------------------+---------------+
# | PASSED   | value returned              | type returned |
# +----------+-----------------------------+---------------+
# | expected | "The average value is 0.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# | actual   | "The average value is 0.0." | <class 'str'> |
# +----------+-----------------------------+---------------+
# 
# 
# ############### function: getLength, score: 1/1###############
# 4 cases were tested
# case 0
# inputs: (3, 4, 'H')
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 5.0            | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 5.0            | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# case 1
# inputs: (5, 12, 'H')
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 13.0           | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 13.0           | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# case 2
# inputs: (13, 5, 'S')
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 12.0           | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 12.0           | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# case 3
# inputs: (5, 3, 'S')
# +----------+----------------+-----------------+
# | PASSED   | value returned | type returned   |
# +----------+----------------+-----------------+
# | expected | 4.0            | <class 'float'> |
# +----------+----------------+-----------------+
# | actual   | 4.0            | <class 'float'> |
# +----------+----------------+-----------------+
# 
# 
# 
# 
# 
# 
# 
# Have trouble completing this assignment? Get help during the following OH/Study Group Sessions:
# APOORV ADITYA  (also requesting all queries over grading of discussion assignments) -:
# Email:
# apoorv-aditya@uiowa.edu
# 
# Study groups-:
# Monday 4:30 pm to 5:30 pm (301 MLH) 
# Tuesday 6 pm to 7 pm (301 MLH) 
# 
# Office hours-: 
# Mon 12:30 pm to 1:30 pm (101N MLH)
# Tue 3:30 pm to 5:30 pm (101N MLH) 
#  
# Rentian Dong  (direct all queries on Programming Assignment grading to him):
# Email:
# rentian-dong@uiowa.edu
#  
# Office hours:
# Thur 6:00 pm to 7:00 pm (301 MLH)
# Fri 3:30 pm - 5:30 pm (301 MLH) 
#  
# Jessica Lu 
# Email:
# jessica-lu@uiowa.edu
# 
# Study groups:
# Wednesday 6:30 pm to 7:30 pm (B13 MLH)
# Thur 4pm to 5pm (B13 MLH) 
# 
# Office hours:
# Wednesday 4:30 pm to 5:30 pm (301 MLH)
# Friday  10am to 12pm (B13 MLH)
# 