'''
Create an empty list called “nums”. Ask the user to enter numbers.
After each number is entered, add it to the end of the nums list and
display the list. Once they have entered three numbers, ask them if
they still want the last number they entered saved. If they say “no”,
remove the last item from the list. Display the list of numbers.
'''

nums = []
num1 = int(input("Enter a number: "))
nums.append(num1)
num2 = int(input("Enter a number: "))
nums.append(num2)
num3 = int(input("Enter a number: "))
nums.append(num3)
choice = input("Do you still want the last number saved? (yes/no)").lower()
if choice == "no":
    nums.remove(num3)
print(nums)
