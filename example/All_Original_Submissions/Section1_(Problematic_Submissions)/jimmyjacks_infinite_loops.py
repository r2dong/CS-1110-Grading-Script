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