import math

POINTS = [(7,2),(4,3),(2,5),(3,7),(12,6),(9,8),(15,5),(12,4),(8,1),(9,5),(7,5),(6,6),(7,7),(8,9),(13,8),(13,2),(10,3),(5,8),(14,7),(14,3)]


outerPoints = []
pointsToDel = []
Done = False


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


def angleBetweenVectors(A, B, C): #Angle between 2 vectors with A common point
    v1 = (A[0]-B[0], A[1]-B[1])
    v2 = (A[0]-C[0], A[1]-C[1])
    res = ((v1[0]*v2[0])+(v1[1]*v2[1])) / ((math.sqrt(v1[0]**2 + v1[1]**2))*(math.sqrt(v2[0]**2 + v2[1]**2)))
    return math.acos(res)


# find outer x coords and y coords
highestX = (0,0)
lowestX = (99999999999999999,99999999999999999)
highestY = (0,0)
lowestY = (99999999999999999,99999999999999999)

for point in POINTS:
    if point[0] > highestX[0]: # highest x coords
        highestX = point
    elif point[0] < lowestX[0]: # lowest x coords
        lowestX = point

    if point[1] > highestY[1]: # highest y coords
        highestY = point
    elif point[1] < lowestY[1]: # lowest y coords
        lowestY = point

outerPoints.append(lowestX)    
outerPoints.append(highestY)    
outerPoints.append(highestX)    
outerPoints.append(lowestY)

POINTS.remove(lowestY)
POINTS.remove(lowestX)
POINTS.remove(highestY)
POINTS.remove(highestX)


# delete points in up and down triangle
for point in POINTS:
    if isInTriangle(lowestX, highestY, highestX, point):
        pointsToDel.append(point)
    
    elif isInTriangle(lowestX, lowestY, highestX, point):
        pointsToDel.append(point)
    
for item in pointsToDel:
    POINTS.remove(item)
pointsToDel.clear()

#create relative middle point
relMiddle = (round((highestX[0] + lowestX[0])/2) , round((highestY[1] + lowestY[1])/2))


startpoint = outerPoints[0]

while not Done:
    smollestAngle = 6.57
    workingPoints = []
    for point in outerPoints:
        angle = angleBetweenVectors(relMiddle, startpoint, point)
        if angle > 0 and angle < smollestAngle and point != startpoint:
            nextPoint = point
        
    for point in POINTS:
        angle = angleBetweenVectors(relMiddle, startpoint, point)
        if angle > 0 and angle < smollestAngle:
            workingPoints.append(point)

    largestDist = 0
    for point in workingPoints:
        if distance(startpoint, nextPoint, point) > largestDist:
            farestPoint = point

    workingPoints.remove(farestPoint)
    outerPoints.append(farestPoint)
    POINTS.remove(farestPoint)

    for point in workingPoints:
        if isInTriangle(startpoint, farestPoint, nextPoint, point):
            POINTS.remove(point)

    if not POINTS:
        Done = True

    startpoint = nextPoint



print (outerPoints)

