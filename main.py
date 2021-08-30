A = (-6.35,-2.15)
B = (-2,4)
C = (3.5,-1)

D = (2.4,0)

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
    

print(isInTriangle(A,B,C,D))