'''
Ask the user to enter a number that is under 20. If they enter a number
that is 20 or more, display the message "Too high", otherwise display
"Thank you".
'''

num = int(input('Enter a number that is under 20:'))

if num >= 20:
    print("Too high!")
else:
    print("Thank you!")


'''
Author's solution:

num = int(input('Enter a value less than 20: '))
if num >= 20:
    print("Too high!")
else:
    print("Thank you!")
'''
    
