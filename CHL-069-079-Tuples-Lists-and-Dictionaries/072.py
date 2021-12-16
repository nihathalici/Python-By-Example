'''
Create a list of six school subjects. Ask the user which of these subjects
they don’t like. Delete the subject they have chosen from the list before
you display the list again.
'''

sbj_lst = ['English', 'Math', 'Science', 'Fine Arts', 'Social Studies', 'Physics']

dlt_sbj = input('Which of these subjects you didn\'t like? ')

sbj_lst.remove(dlt_sbj)

print(sbj_lst)


'''
Author's solution:

subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
print(subject_list)
dislike = input("Which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)
'''
