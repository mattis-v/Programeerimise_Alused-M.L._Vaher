def dist(points):
    point1 = max(points)
    point2 = min(points)
    return(point1-point2)

print(dist([1,2,3,4,5]))