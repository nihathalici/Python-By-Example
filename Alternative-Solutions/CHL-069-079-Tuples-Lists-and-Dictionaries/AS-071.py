'''
AS-071
Create a list of two sports. Ask the user what their favourite sport
is and add this to the end of the list. Sort the list and display 
'''
#####
# Python By Example
# Exercise 071
# Christopher Hagan
#####

sportsList = ['Gaelic', 'Hurley']
sportsList.append(input('Enter your favourite sport: '))
sportsList.sort()
print(sportsList)




