'''
Write a program that will ask for a number of days and then will show
how many hours, minutes and seconds are in that number of days.
'''

#####
# Python By Example
# Exercise 009
# Christopher Hagan
#####

numberOfDays = int(input('Enter the number of days to convert into hours, minutes and seconds: '))

print('{} days = {} hours = {} minutes = {} seconds'.format(numberOfDays, (numberOfDays * 24), (numberOfDays * 1440), (numberOfDays * 86400)))
