'''
AS-073
Ask the user to enter four of their favourite foods and store them in a dictionary
so that they are indexed with numbers starting from 1. Display the dictionary in full,
showing the index number and the item. Ask them which they want to get rid of and
remove it from the list. Sort the remaining data and display the dictionary.
'''

#####
# Python By Example
# Exercise 073
# Christopher Hagan
#####

foods = {}

for i in range(1, 5):
    favouriteFood = input('Enter one of your favourite foods: ')
    foods[i] = favouriteFood

print(foods)

foods.pop(int(input('Which food by index should be removed: ')))

print(sorted(foods.values()))
    
