'''
AS-019
Ask the user to enter 1, 2 or 3. If they enter a 1, display the message
"Thank you", if they enter a 2, display "Well done", if they enter a 3,
display "Correct". If they enter anything else, display "Error message".
'''
#####
# Python By Example
# Exercise 019
# Christopher Hagan
#####

number = int(input('Please enter 1, 2 or 3: '))

if number == 1:
    print('Thank you!')
elif number == 2:
    print('Well done!')
elif number == 3:
    print('Correct!')
else:
    print('Error message!')
