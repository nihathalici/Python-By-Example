'''
AS-086
Ask the user to enter a new password. Ask them to enter it again.
If the two passwords match, display “Thank you”. If the letters
are correct but in the wrong case, display the message “They must
be in the same case”, otherwise display the message “Incorrect”.
'''
#####
# Python By Example
# Exercise 086
# Christopher Hagan
#####

newPass = input('Please enter a new password: ')
reenterPass = input('Please re-enter the password: ')

if newPass == reenterPass:
    print('Thank you')
elif newPass.lower() == reenterPass.lower():
    print('They must be in the same case')
else:
    print('Incorrect')
