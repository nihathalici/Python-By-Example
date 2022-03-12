'''
Create an empty list called “nums”. Ask the user to enter numbers.
After each number is entered, add it to the end of the nums list and
display the list. Once they have entered three numbers, ask them if
they still want the last number they entered saved. If they say “no”,
remove the last item from the list. Display the list of numbers.
'''
#####
# Python By Example
# Exercise 079
# Christopher Hagan
#####

nums = []
count = 0
while count < 3:
    nums.append(int(input('Enter a number: ')))
    print(nums)
    count += 1

wantLastNumber = input('Do you still want the last number? ')
if wantLastNumber.lower().startswith('n'):
    nums.remove(nums[-1])

print(nums)

