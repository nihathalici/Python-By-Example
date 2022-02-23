'''
AS-040
Ask for a number below 50 and then count down from 50
to that number, making sure you show the number they
entered in the output.
'''
  
#####
# Python By Example
# Exercise 040
# Christopher Hagan
#####

number = int(input('Please enter a number less than 50 so I can count down to it: '))
for i in range(50, number, -1):
    print(i)
