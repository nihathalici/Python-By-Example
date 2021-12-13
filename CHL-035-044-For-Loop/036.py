'''
Alter program 035 so that it will ask the user to enter their name and
a number and then display their name that number of times.
'''

name = input('Enter your name: ')
num  = int(input('Enter a number: '))
for i in range(0, num):
    print(name)
