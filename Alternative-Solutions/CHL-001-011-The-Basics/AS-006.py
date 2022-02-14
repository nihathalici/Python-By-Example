'''
Ask how many slices of pizza the user started with and ask how many slices
they have eaten. Work out how many slices they have left and display
the answer in a user- friendly format.
'''

#####
# Python By Example
# Exercise 006
# Christopher Hagan
#####

totalSlices = int(input('How many slices of Pizza did you start with? '))
eatenSlices = int(input('And how many slices have since been eaten? '))
print('You have {} slices remaining.'.format(totalSlices - eatenSlices))
