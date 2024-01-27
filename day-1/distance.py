from math import sqrt

def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)

pointA = (2, 3)
pointB = (10, 8)
distance = dist(pointA, pointB)
print(f"The euclidean distance between {pointA} and {pointB} is {distance}")