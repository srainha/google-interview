def points_are_square(points):
    a, b, c, d = points
    anchor = a
    dist_1 = distance(a, b)
    dist_2 = distance(a, c)
    dist_3 = distance(a, d)
    if (dist_1 == dist_2): return (distance(c, d) == distance(b, d))
    if (dist_2 == dist_3): return (distance(c, b) == distance(b, d))
    if (dist_1 == dist_3): return (distance(c, d) == distance(b, c))
    return False

def distance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - 
point_2[1])**2
