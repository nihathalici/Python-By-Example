'''
AS-018
Ask the user to enter a number. If it is under 10, display the message "Too low",
if their number is between 10 and 20, display "Correct", otherwise display
"Too high".
'''

####
# Python By Example
# Exercise 018
# Christopher Hagan
#####

number = int(input('Enter a number: '))

if number < 10:
    print('Too low!')
elif number >=10 and number <= 20:
    print('Correct!')
else:
    print('Too high!')
