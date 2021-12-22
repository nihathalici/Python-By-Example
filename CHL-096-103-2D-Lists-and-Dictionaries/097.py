'''
Using the 2D list from program 096, ask the user to
select a row and a column and display that value.
'''
data_set = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row: "))
col = int(input("Select a column: "))

print(data_set[row][col])
