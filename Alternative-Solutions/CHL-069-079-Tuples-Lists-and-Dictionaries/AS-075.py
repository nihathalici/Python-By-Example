'''
AS-075
Create a list of four three-digit numbers. Display the list to the user,
showing each item from the list on a separate line. Ask the user to enter
a three-digit number. If the number they have typed in matches one in the list,
display the position of that number in the list, otherwise display the message
“That is not in the list”.
'''

#####
# Python By Example
# Exercise 075
# Christopher Hagan
#####

numbersList = [436, 745, 897, 603]

for i in range(0, len(numbersList)):
    print(numbersList[i])

userNumber = int(input('Enter a three digit number: '))
if userNumber in numbersList:
    print('This is the number with index {}'.format(numbersList.index(userNumber)))
else:
    print('This is not in the list.')




    
