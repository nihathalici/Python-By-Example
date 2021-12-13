'''
Change program 037 to also ask for a number.
Display their name (one letter at a time on
each line) and repeat this for the number
of times they entered.
'''

name = input('Enter your name: ')
num  = int(input('Enter a number: '))

for x in range(0, num):
    for i in name:
        print(i)
