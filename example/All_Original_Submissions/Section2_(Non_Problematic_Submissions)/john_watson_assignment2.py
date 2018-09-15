# Problem 1: A function which takes no arguments and returns my HawkID!
def getHawkIDs():
    return ["jwatson"]

# Problem 2 : A function that takes as arguments the X and Y coordinates of two points and returns a list containing the X and Y coordinates of the midpoint for that line segment. The values are rounded to the nearest .1. 

def getMidpoint(x1,y1,x2,y2):
   #Create a list to store the data within. 
    midpointList = []
    #Doing the calculation to produce the decimals (unrounded)
    xMidpoint= ((float(x1) + float(x2))/2.0)
    yMidpoint= ((float(y1) + float(y2))/2.0)
    # Rounding the values using the round function. 
    xMidpoint = round(xMidpoint,1)
    yMidpoint = round(yMidpoint,1)
   #Appending the list with the values
    midpointList.append(xMidpoint)
    midpointList.append(yMidpoint)
    return midpointList

# Problem 3: A function that takes, as arguments, 5 values and returns the average of those values, rounded to the nearest 10th.

def getAverage(p1,p2,p3,p4,p5):
    # Doing the calculation. Not sure if I need the float() here but hey it can't hurt right. 
    average = float((p1+p2+p3+p4+p5)/5.0)
    # Rounding the float 
    average = round(average,1)
    return average

# Problem 4: A function that takes, as arguments, 5 values and returns a string describing the average of those values rounded to the nearest 10th. 

def getAverageString(p1,p2,p3,p4,p5):
    # Doing the calculation.
    average = float((p1+p2+p3+p4+p5)/(5.0))
    # Rounding 
    average = round(average,1)
    return str("The average value is " + str(average) + ".")

# Problem 5: A function that takes as arguments, two values representing the length of two sides of a right angled triangle. Returns the length of the third side of the triangle. 

def getLength(p1,p2,myString):
  #Producing variables
    finalLength = 0
    h = 0
    s = 0
    
    # H condition
    if (myString =="H"):
        h = (p1**2+p2**2)**0.5
        h = round(h,1)
        finalLength = h 
        
   # S condition 
    elif (myString == "S"):
        s = (p1**2 - p2**2)**0.5
       # Exception checking incase P2 is larger than P1. **0.5 of that will always produce a number with some factor or i so I ran a complex number check. 
        if type(s) == complex: 
            s = (p2**2 - p1**2)**0.5
        #Returns the value to the variable 
        finalLength = s 
    
    #Rounding
    return round(finalLength,1)
            
        
        
        
    