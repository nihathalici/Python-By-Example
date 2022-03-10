'''
AS-074
Enter a list of ten colours. Ask the user for a starting number between 0 and 4
and an end number between 5 and 9. Display the list for those colours between
the start and end numbers the user input.
'''
#####
# Python By Example
# Exercise 074
# Christopher Hagan
#####

coloursList = ['Red', 'Green', 'Blue', 'Purple', 'Orange', 'White', 'Black', 'Grey', 'Pink', 'Yellow']

print(coloursList)
startIndex = int(input('Enter the start index(0-4): '))
endIndex = int(input('Enter the end index(5-9): '))
print(coloursList[startIndex:endIndex])
