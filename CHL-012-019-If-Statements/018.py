'''
Ask the user to enter a number. If it is under 10, display the message "Too low",
if their number is between 10 and 20, display "Correct", otherwise display
"Too high".
'''

num = int(input("Enter a number: "))

if num > 10 and num < 20:
    print("Correct")
elif num < 10:
    print("Too low")
else:
    print("Too high")
