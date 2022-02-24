'''
AS-042
Set a variable called total to 0. Ask the user to enter five numbers and
after each input ask them if they want that number included. If they do,
then add the number to the total. If they do not want it included, don’t
add it to the total. After they have entered all five numbers, display
the total.
'''
  
#####
# Python By Example
# Exercise 042
# Christopher Hagan
#####

total = 0
for i in range(0, 5):
    num = int(input('Please enter a number: '))
    addToTotal = input('Should this be added to the total? ')
    if addToTotal.lower().startswith('y'):
        total += num

print('The total is {}'.format(total))














        
