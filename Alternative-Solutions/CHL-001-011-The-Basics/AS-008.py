'''
Ask for the total price of the bill, then ask how many diners there are. Divide
the total bill by the number of diners and show how much each person must pay.
'''

#####
# Python By Example
# Exercise 008
# Christopher Hagan
#####

totalPrice = float(input('What was the total price of the bill? £'))

numberOfDiners = int(input('And how many diners were present? '))

print('The total cost of the bill each is £ {}.'.format(totalPrice / numberOfDiners))
