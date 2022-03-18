'''
Ask the user to enter a new password. Ask them to enter it again.
If the two passwords match, display “Thank you”. If the letters
are correct but in the wrong case, display the message “They must
be in the same case”, otherwise display the message “Incorrect”.
'''

inp1 = input("Enter a new pword: ")

inp2 = input("Enter pword again: ")

if inp1 == inp2:
    print("Thank you!")
elif (inp1.isupper() and inp2.islower()) or (inp1.islower() and inp2.isupper()):
    print("They must be in the same case")
else:
    print("Incorrect")
    
