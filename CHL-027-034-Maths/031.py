'''
Ask the user to enter the radius of a circle (measurement from the centre
point to the edge). Work out the area of the circle (π*radius2).
'''
import math

my_radius = int(input('Enter the radius of a circle: '))

print( math.pi * (my_radius ** 2) )
