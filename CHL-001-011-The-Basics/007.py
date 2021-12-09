'''
Ask the user for their name and their age. Add 1 to their age and display the output
[Name] next birthday you will be [new age].
'''

name = input('Your name?')
age = int(input('Your age?'))

print('{}, next birthday you will be {}.'.format(name, (age +1)))

'''
Author's solution:

name = input('What is your name? ')
age = int(input('How old are you? '))
newAge = age + 1
print(name, "next birthday you will be", newAge)
'''
