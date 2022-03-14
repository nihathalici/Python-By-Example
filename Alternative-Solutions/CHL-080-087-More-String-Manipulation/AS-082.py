'''
AS-082
Show the user a line of text from your favourite poem and ask for a starting
and ending point. Display the characters between those two points.
'''
#####
# Python By Example
# Exercise 082
# Christopher Hagan
#####

firstLine = 'Baby on board, something, something Bert Ward!'
print(firstLine)
startPoint = int(input('Enter the starting point for the snippet: '))
endPoint = int(input('Enter the ending point for the snippet: '))
print('Snippet: {}'.format(firstLine[startPoint:endPoint]))
