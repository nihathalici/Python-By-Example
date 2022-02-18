'''
AS-023
Ask the user to type in the first line of a nursery rhyme and display
the length of the string. Ask for a starting number and an ending number
and then display just that section of the text (remember Python starts
counting from 0 and not 1).
'''
#####
# Python By Example
# Exercise 023
# Christopher Hagan
#####

firstLine = input('Enter the first line of a nursery rhyme: ')
print('\nYour line is {} characters long.'.format(len(firstLine)))

start = int(input('I will now display only part of the rhyme at which character number should I start? '))
end = int(input('And I should stop at character? '))
print(firstLine[start:end])
