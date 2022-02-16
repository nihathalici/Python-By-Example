'''
AS-015
Ask the user to enter their favourite colour. If they enter "red", "RED" or
"Red" display the message "I like red too", otherwise display the message
"I don’t like [colour], I prefer red".
'''

#####
# Python By Example
# Exercise 015
# Christopher Hagan
#####

colour = input('What is your favourite colour? ')

if colour.lower() == 'red':
    print('I like red too!')
else:
    print('I don\'t like {}, I prefer red.'.format(colour))
