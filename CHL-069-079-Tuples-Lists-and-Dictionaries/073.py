'''
Ask the user to enter four of their favourite foods and store them in a dictionary
so that they are indexed with numbers starting from 1. Display the dictionary in full,
showing the index number and the item. Ask them which they want to get rid of and
remove it from the list. Sort the remaining data and display the dictionary.
'''

food_dict = {}
food1 = input("Enter a food you like: ")
food_dict[1] = food1
food2 = input("Enter another food:")
food_dict[2] = food2
food3 = input("Enter another food:")
food_dict[3] = food3
food4 = input("Enter another food:")
food_dict[4] = food4
print(food_dict)
dislike = int(input("Which of these do you want to get rid of? "))
del food_dict[dislike]
print(sorted(food_dict.values()))
