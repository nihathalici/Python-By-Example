'''
Create a list containing the titles of four TV programmes and display them
on separate lines. Ask the user to enter another show and a position they
want it inserted into the list. Display the list again, showing all five
TV programmes in their new positions.
'''

tv_pr_lst = ["tv_pr_1", "tv_pr_2", "tv_pr_3", "tv_pr_4"]

for item in tv_pr_lst:
    print(item)

new_item = input("Enter another TV show: ")
new_pos = int(input("Enter index position: "))

tv_pr_lst.insert(new_pos, new_item)

for item in tv_pr_lst:
    print(item)
