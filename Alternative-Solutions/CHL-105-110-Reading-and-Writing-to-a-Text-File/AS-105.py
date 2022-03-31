'''
AS-105
Write a new file called “Numbers.txt”. Add five numbers to the document
which are stored on the same line and only separated by a comma. Once you
have run the program, look in the location where your program is
stored and you should see that the file has been created. The easiest way to
view the contents of the new text file on a Windows system is to read it
using Notepad.
'''

#####
# Python By Example
# Exercise 105
# Christopher Hagan
#####

file = open('AS_Numbers.txt', 'w')
for i in range(5, 26, 5):
    file.write("{}, ".format(i))

file.close()
