'''
AS-072
Create a list of six school subjects. Ask the user which of these subjects
they don’t like. Delete the subject they have chosen from the list before
you display the list again.
'''
#####
# Python By Example
# Exercise 072
# Christopher Hagan
#####

subjectsList = ['English', 'Maths', 'History', 'Computing', 'Physics', 'Chemistry']
print(subjectsList)
subjectsList.remove(input('Which subject should be removed from this list: '))
print(subjectsList)

