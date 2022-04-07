'''
AS-118
Define a subprogram that will ask the user to
enter a number and save it as the variable
“num”. Define another subprogram that will
use “num” and count from 1 to that number.
'''

#####
# Python By Example
# Exercise 118
# Christopher Hagan
#####

def getNum():
    isNumber = False
    while not isNumber:
        enteredNumber = input('Please enter a number: ')
        try:
            num = int(enteredNumber)
            isNumber = True
        except:
            print('This is not a valid number, try again!')
    return num

def countToNum(num):
    for i in range(0, num):
        print('{}, '.format(i+1), end='')


countToNum(getNum())