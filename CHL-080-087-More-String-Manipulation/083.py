'''
Ask the user to type in a word in upper case. If they type it in lower case,
ask them to try again. Keep repeating this until they type in a message all
in uppercase.
'''

inp = input("Type in a word in upper case: ")

while inp.islower():
    print("Please try again: ")
    inp = input("Type in a word in upper case: ")
print(inp)

'''
Author's solution:

msg = input("Enter a message in uppercase: ")
tryagain = False
while tryagain == False:
    if msg.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again")
        msg = input("Enter a message in uppercase: ")

'''
