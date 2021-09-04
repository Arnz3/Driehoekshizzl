import math

POINTS = []


def isInTriangle(pointA, pointB, pointC, pointD):
    #make vectors
    v = pointD
    v0 = pointA
    v1 = (pointB[0] - pointA[0], pointB[1] - pointA[1])
    v2 = (pointC[0] - pointA[0], pointC[1] - pointA[1])

    a = (round(v[0]*v2[1]-v[1]*v2[0]) - round(v0[0]*v2[1]-v0[1]*v2[0])) / (round(v1[0]*v2[1]-v1[1]*v2[0]))
    if a < 0:
        return False
    
    b = - (round(v[0]*v1[1]-v[1]*v1[0]) - round(v0[0]*v1[1]-v0[1]*v1[0])) / (round(v1[0]*v2[1]-v1[1]*v2[0]))

    if b < 0:
        return False

    if (a + b >= 1):
        return False

    else:
        return True


def distance(A, B, V): # distance between point and line
    return abs((B[0]-A[0])*(A[1]-V[1])-(A[0]-V[0])*(B[1]-A[1])) / math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)


def pointIsClockwise(A, B, V):
    v1 = (B[0]-A[0], B[1]-A[1])
    v2 = (B[0]-V[0], B[1]-V[1])
    cp = v1[0]*v2[1] - v1[1]*v2[0]

    if cp > 0:
        return False
    elif cp < 0:
        return True
    elif cp == 0:
        Exception("crossproduct is 0")


# find outer x coords and y coords
highestX = (0,0)
lowestX = (0,0)
highestY = (0,0)
lowestY = (0,0)

for point in POINTS:
    if point[0] > highestX[0]: # highest x coords
        highestX = point
    elif point[0] < lowestX[0]: # lowest x coords
        lowestX = point

    if point[1] > highestY[1]: # highest y coords
        highestY = point
    elif point[1] < lowestY[1]: # lowest y coords
        lowestY = point    


# delete points in up and down triangle
for point in POINTS:
    if isInTriangle(lowestX, highestY, highestX, point):
        POINTS.remove(point)
    
    if isInTriangle(lowestX, lowestY, highestX, point):
        POINTS.remove(point)
    

# sort resting points per kwadrant
'''
kw1 = []
kw2 = []
kw3 = []
kw4 = []

for point in POINTS:
    if point[0] < highestY[0] and point[1] > lowestX[1]:
        kw1.append(point)
    elif point[0] > highestY[0] and point[1] > highestX[1]:
        kw2.append(point)
    elif point[0] > lowestY[0] and point[1] < highestX[1]:
        kw3.append(point)
    elif point[0] < lowestY[0] and point[1] < lowestX[1]:
        kw3.append(point) 
'''

# calculating each kwadrant
#--> kw1
def calcKwadrant(A , B , clockwise):
    workingPoints = []

    for point in POINTS:
        if point == A or point == B:
            pass
        elif pointIsClockwise(A, B, point) == clockwise:
            workingPoints.append(point)

    longestDist = 0
    for point in workingPoints:
        if distance(A, B, point) > longestDist:
            longestDist = distance(A, B, point)
            fardestPoint = point

    workingPoints.remove(fardestPoint)

    for point in workingPoints:
        if isInTriangle(A, B, fardestPoint, point):
            POINTS.remove(point)
            workingPoints.remove(point)
    
    if not workingPoints:
        return
    else:
        pass # TODO figure out wtf i have to do
    


