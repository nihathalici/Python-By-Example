'''
Create a list containing the titles of four TV programmes and display them
on separate lines. Ask the user to enter another show and a position they
want it inserted into the list. Display the list again, showing all five
TV programmes in their new positions.
'''

#####
# Python By Example
# Exercise 078
# Christopher Hagan
#####

listOfProgrammes = ['Dark', 'Mr Robot', 'Vikings', 'Curb Your Enthusiasm']

for i in range(0, len(listOfProgrammes)):
    print(listOfProgrammes[i])

newProgramme = input('Enter the name of another TV show: ')

positionValue = int(input('Which position index in the list should this show take: '))

listOfProgrammes.insert(positionValue, newProgramme)

print(listOfProgrammes)
