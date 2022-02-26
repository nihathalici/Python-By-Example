
'''
AS-050
Ask the user to enter a number between 10 and 20. If they enter a value under 10,
display the message “Too low” and ask them to try again. If they enter a value
above 20, display the message “Too high” and ask them to try again. Keep repeating
this until they enter a value that is between 10 and 20 and then display the message
“Thank you”.
'''

####
# Python By Example
# Exercise 050
# Christopher Hagan
#####

num = 0

while num < 10 or num > 20:
    num = int(input('Please enter a number between 10 and 20: '))
    if num < 10:
        print('Too low, please try again!')
    elif num > 20:
        print('Too high, please try again!')

print('Thank you!')
