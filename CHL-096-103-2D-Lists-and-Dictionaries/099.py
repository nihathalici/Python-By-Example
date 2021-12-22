'''
Change your previous program to ask the user which row they
want displayed. Display that row. Ask which column in that
row they want displayed and display the value that is held
there. Ask the user if they want to change the value.
If they do, ask for a new value and change the data.
Finally, display the whole row again.
'''
data_set = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Which row? "))
print(data_set[row])
col = int(input("Which column? "))
print(data_set[row][col])
choice = input("Do you want  to change the value? (y/n)")
if choice == 'y':
    new_val = int(input("Enter the new value: "))
data_set[row][col] = new_val
print(data_set[row])
