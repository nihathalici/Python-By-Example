'''
Create a list of four three-digit numbers. Display the list to the user,
showing each item from the list on a separate line. Ask the user to enter
a three-digit number. If the number they have typed in matches one in the list,
display the position of that number in the list, otherwise display the message
“That is not in the list”.
'''

num_lst = [100, 500, 999]
for num in num_lst:
    print(num)
user_entry = int(input("Enter a three-digit number: "))
if user_entry in num_lst:
    print("{} is in the list index number: {}".format(user_entry, num_lst.index(user_entry)))
else:
     print("That is not in the list")
