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
            
        
        
        
    




# ###############function: getHawkIDs, score: 1/1###############
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