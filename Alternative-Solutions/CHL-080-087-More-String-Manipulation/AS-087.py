'''
AS-087
Ask the user to type in a word and then display it
backwards on separate line.
'''

#####
# Python By Example
# Exercise 087
# Christopher Hagan
#####

word = input('Enter a word: ')
for i in range(len(word), 0, -1):
    print(word[i-1])
