'''
AS-038
Change program 037 to also ask for a number.
Display their name (one letter at a time on
each line) and repeat this for the number
of times they entered.
'''

#####
# Python By Example
# Exercise 038
# Christopher Hagan
#####

name = input('Please enter your name: ')
repetitions = int(input('How many times should I loop through the characters in'
                        ' your name? '))


for i in range(0, repetitions):
    print(name[i % len(name)])









