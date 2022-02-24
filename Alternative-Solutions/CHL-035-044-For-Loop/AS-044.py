'''
AS-044
Ask how many people the user wants to invite to a party. If they enter
a number below 10, ask for the names and after each name display
“[name] has been invited”. If they enter a number which is 10 or higher,
display the message "Too many people".
'''

#####
# Python By Example
# Exercise 044
# Christopher Hagan
#####

number = int(input('How many people would you like to invite to your party? '))
if number < 10:
    for i in range(0, number):
        guest = input('Enter the name of your next guest: ')
        print('{} has been invited.'.format(guest))
else:
    print('Too many people!')
                     
