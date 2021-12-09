'''
Ask for the total price of the bill, then ask how many diners there are. Divide
the total bill by the number of diners and show how much each person must pay.
'''

total_price = int(input('The total price of the bill?'))
diners = int(input('How many diners?'))

print('Each person must pay {}.'.format(total_price / diners))



'''
Author's solution:

bill = int(input('What is the total cost of the bill? '))
people = int(input('How many people are there? '))
each = bill/people
print("Each person should pay £", each)
