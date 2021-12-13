'''
Ask the user to enter a number between 1 and 12
and then display the times table for that number.
'''

num  = int(input('Enter a number between 1 and 12: '))

for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)
