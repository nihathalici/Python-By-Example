'''
AS-041
Ask the user to enter their name and a number. If the number is less than 10,
then display their name that number of times; otherwise display the message
"Too high" three times.
'''
  
#####
# Python By Example
# Exercise 041
# Christopher Hagan
#####

name = input('Please enter your name: ')
repetitions = int(input('How many times should I repeat your name: '))

if repetitions < 10:
    textToRepeat = name
else:
    textToRepeat = 'Too high'
    repetitions = 3

for i in range(0, repetitions):
    print(textToRepeat)
