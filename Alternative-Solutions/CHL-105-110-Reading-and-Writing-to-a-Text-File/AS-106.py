'''
AS-106
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
'''

#####
# Python By Example
# Exercise 106
# Christopher Hagan
#####

file = open('AS_Names.txt', 'w')
for name in ('Chris', 'Hannah', 'Lochlann', 'Rex', 'Emmet'):
    file.write('{}\n'.format(name))

file.close()
