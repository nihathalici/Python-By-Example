'''
AS-069
Create a tuple containing the names of five countries and display the whole tuple.

Ask the user to enter one of the countries that have been shown to them and then
display the index number (i.e. position in the list) of that item in the tuple.
'''

#####
# Python By Example
# Exercise 069
# Christopher Hagan
#####

countriesTuple = ('Iceland', 'Greenland', 'Norway', 'Finland', 'Sweden')

print('Some countries are : {}'.format(countriesTuple))
userChoice = input('Enter one of the countries: ')
print('This country has index {} in the tuple.'.format(countriesTuple.index(userChoice)))
