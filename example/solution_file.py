def getHawkIDs():
    return ["rdong6"]

def getMidpoint(x1, y1, x2, y2):
    return [round((x1 + x2) / 2.0, 1), round((y1 + y2) / 2.0, 1)]

def getAverage(p1, p2, p3, p4, p5):
    return round((p1 + p2 + p3 + p4 + p5) / 5.0, 1)

def getAverageString(p1, p2, p3, p4, p5):
    return "The average value is " + str(getAverage(p1, p2, p3, p4, p5)) + "."

def getLength(p1, p2, myString):
    if myString == "H":
        return round((p1 ** 2 + p2 ** 2) ** 0.5, 1)
    elif myString == "S":
        return round(abs(p1 ** 2 - p2 ** 2) ** 0.5, 1)

