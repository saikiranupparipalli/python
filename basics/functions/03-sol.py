import math
def area_circumference_of_circle(r):
    area = round(3.14 * (r ** 2), 1) 
    circumference = 2 * round((math.pi * r), 1)
    return area, circumference
    
a, c = area_circumference_of_circle(5)
print('area:', a, '|', 'circumference:', c)
# round method