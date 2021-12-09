'''
Write a program that will ask for a number of days and then will show
how many hours, minutes and seconds are in that number of days.
'''


number_of_days = int(input('How many days?'))

print('{} days are {} hours, {} minutes, and {} seconds.'.format(number_of_days,
                                                                (number_of_days*24),
                                                                (number_of_days * 1440),
                                                                (number_of_days * 86400)))

'''
Author's solution:

days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In", days, "days there are..")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")
'''
