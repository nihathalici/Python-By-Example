'''
AS-034
Display the following message:
1) Square
2) Triangle

Enter a number:

If the user enters 1, then it should ask them for the length of one of
its sides and display the area. If they select 2, it should ask for the
base and height of the triangle and display the area. If they type in
anything else, it should give them a suitable error message.
'''

#####
# Python By Example
# Exercise 034
# Christopher Hagan
#####

shape = input("1) Square\n2) Triangle\n\nEnter a number: ")

if shape == '1':
    length = int(input('Enter the length of one of the sides of the Square: '))
    print('The area of your Square is {}'.format(length**2))
elif shape = '2':
    height = int(input('Enter the height of the Triangle: '))
    breadth = int(input('Enter the breadth of the Triangle: '))
    print('The area of your Triangle is {}'.format((height * breadth) / 2))
else:
    print('Invalid option!')
