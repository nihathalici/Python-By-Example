'''
AS-028
Update program 027 so that it will display the answer to two decimal places.
'''

#####
# Python By Example
# Exercise 028
# Christopher Hagan
#####

num = float(input('Enter a number with many decimal places: '))
print('Your number {} multiplied by 2 is {}'.format(num, round(num * 2, 2)))
