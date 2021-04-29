import math

def distance(first_point, second_point):
    x1 = first_point[0]
    x2 = second_point[0]
    y1 = first_point[1]
    y2 = second_point[1]
    power1 = pow(y2-y1, 2)
    power2 = pow(x2-x1, 2)
    return math.sqrt(power1 + power2)

# This should print 5.0
print distance((1, 1), (4, 5))