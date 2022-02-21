'''
AS-032
Ask for the radius and the depth of a cylinder and work out the total volume
(circle area*depth) rounded to three decimal places.
'''

#####
# Python By Example
# Exercise 032
# Christopher Hagan
#####

import math

radius = float(input('Enter the radius of a cylinder: '))
length = float(input('Enter the length of the cylinder: '))

print('If r={} and l={} the volume of this circle would be {}'.format(radius, length, length*math.pi*(radius**2)))
