'''
AS-043
Ask which direction the user wants to count (up or down). If they select up,
then ask them for the top number and then count from 1 to that number. If they
select down, ask them to enter a number below 20 and then count down from 20
to that number. If they entered something other than up or down,
display the message "I don’t understand".

'''    
    
#####
# Python By Example
# Exercise 043
# Christopher Hagan
#####

direction = input('Would you like to count upwards or downwards? ')
if direction.lower().startswith('u'):
    maxNumber = int(input('Enter the number to count up to: '))
    for i in range(1, maxNumber+1):
        print(i)
elif direction.lower().startswith('d'):
    minNumber = int(input('Enter a number under 20 to count down from 20 to: '))
    for i in range(20, minNumber, -1):
        print(i)
else:
    print('I don\'t understand')




        
