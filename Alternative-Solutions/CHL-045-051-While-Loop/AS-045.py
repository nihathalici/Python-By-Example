
'''
AS-045
Set the total to 0 to start with. While the total is 50 or less,
ask the user to input a number. Add that number to the total and
print the message "The total is... [total]". Stop the loop when
the total is over 50.
'''

#####
# Python By Example
# Exercise 045
# Christopher Hagan
#####

total = 0
while total < 50:
    num = int(input('Enter a number to add to the total: '))
    total += num
    print('The total is now {}'.format(total))

