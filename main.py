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
    pass


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

# calculating each kwadrant
#--> kw1
for point in kw1:
    pass

