'''
AS-031
Ask the user to enter the radius of a circle (measurement from the centre
point to the edge). Work out the area of the circle (π*radius2).
'''

#####
# Python By Example
# Exercise 031
# Christopher Hagan
#####

import math

radius = float(input('Enter the radius of a circle: '))
print('If r={} the area of this circle would be {}'.format(radius, math.pi*(radius**2)))
