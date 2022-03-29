'''
AS-101
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose.
'''

#####
# Python By Example
# Exercise 101
# Christopher Hagan
#####

import sys

salesDictionary = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
                   'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
                   'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
                   'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}

name = input('Please enter the name of the sales person you would like to update: ')
region = input('Please enter the sales region you would like to update: ')

try:
    print('The {} region value for {} is currently {}.'.format(region, name, salesDictionary[name][region]))
except:
    sys.exit('This values does not exist!')

newValue = int(input('Enter the new value for this region: '))
salesDictionary[name][region] = newValue
print(salesDictionary[name])





















