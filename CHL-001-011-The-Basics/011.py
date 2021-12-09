'''
Task the user to enter a number over 100 and then enter a number under 10 and tell them
how many times the smaller number goes into the larger number in a user-friendly format.
'''

number_over = int(input('Enter a number over 100.'))
number_under = int(input('Enter a number under 10.'))

print('Number {} goes {} times into the number {}.'.format(number_under,
                                                          (number_over // number_under),
                                                           number_over))


'''
Author's solution:

larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger//smaller
print(smaller, "goes into", larger, answer,"times")
