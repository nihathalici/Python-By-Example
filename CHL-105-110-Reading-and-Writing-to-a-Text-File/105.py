'''
Write a new file called “Numbers.txt”. Add five numbers to the document
which are stored on the same line and only separated by a comma. Once you
have run the program, look in the location where your program is
stored and you should see that the file has been created. The easiest way to
view the contents of the new text file on a Windows system is to read it
using Notepad.
'''


file = open("Numbers.txt", "w")
file.write('1, 2, 3, 4, 5')
file.close()

"""
Author's solution:

file = open("Numbers.txt", "w")
file.write("4, ")
file.write("6, ")
file.write("10, ")
file.write("8, ")
file.write("5, ")
file.close()
"""
