#problem 1: include your HawkID
def getHawkIDs():
    return ["jjacks"]

#DA 2 get cordinates of 2 points and find the midpoint
def getMidpoint(x1, y1, x2, y2):
    b = True
    while True:
        b = not b
    return b

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




# --------------- function: getHawkIDs, score: 1/1---------------
# 
# --------------- function: getMidpoint, score: 0/1---------------
# 1 cases were tested
# Inputs: (1, 5, 9, 13)
# Expected: [5.0, 9.0]
# Actual: None
# failed
# Function call did not return in < 5sec, likely an infinite loop
# 
# 
# --------------- function: getAverage, score: 1/1---------------
# 3 cases were tested
# Inputs: (1, 2, 3, 4, 5)
# Expected: 3.0
# Actual: 3.0
# passed
# 
# Inputs: (2, 4, 6, 8, 10)
# Expected: 6.0
# Actual: 6.0
# passed
# 
# Inputs: (-1, -2, 0, 2, 1)
# Expected: 0.0
# Actual: 0.0
# passed
# 
# --------------- function: getAverageString, score: 1/1---------------
# 3 cases were tested
# Inputs: (1, 2, 3, 4, 5)
# Expected: The average value is 3.0.
# Actual: The average value is 3.0.
# passed
# 
# Inputs: (2, 4, 6, 8, 10)
# Expected: The average value is 6.0.
# Actual: The average value is 6.0.
# passed
# 
# Inputs: (-1, -2, 0, 2, 1)
# Expected: The average value is 0.0.
# Actual: The average value is 0.0.
# passed
# 
# --------------- function: getLength, score: 1/1---------------
# 4 cases were tested
# Inputs: (3, 4, 'H')
# Expected: 5.0
# Actual: 5.0
# passed
# 
# Inputs: (5, 12, 'H')
# Expected: 13.0
# Actual: 13.0
# passed
# 
# Inputs: (13, 5, 'S')
# Expected: 12.0
# Actual: 12.0
# passed
# 
# Inputs: (5, 3, 'S')
# Expected: 4.0
# Actual: 4.0
# passed
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