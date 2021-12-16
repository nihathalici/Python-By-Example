'''
Enter a list of ten colours. Ask the user for a starting number between 0 and 4
and an end number between 5 and 9. Display the list for those colours between
the start and end numbers the user input.
'''

col_lst = ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black', 'Brown', 'Azure', 'Ivory', 'Purple']

st_num = int(input("Enter a starting number between 0 and 4: "))
en_num = int(input("Enter a end number between 5 and 9: "))

print(col_lst[st_num:en_num])
