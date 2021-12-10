'''
Ask the user to enter their favourite colour. If they enter "red", "RED" or
"Red" display the message "I like red too", otherwise display the message
"I don’t like [colour], I prefer red".
'''

inp = input('Enter your favourite colour:')

if inp == 'RED' or inp == 'Red' or inp == 'red':
    print("I like red too!")
else:
    print("I don’t like {}, I prefer red!".format(inp))

'''
Author's solution:

colour = input("Type in your favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too.")
else:
    print("I don't like that colour, I prefer red")

'''
