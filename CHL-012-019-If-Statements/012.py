'''
Ask for two numbers. If the first one is larger than the second, display
the second number first and then the first number, otherwise show the first
number first and then the second.
'''

fi_num = int(input('First number:'))
sec_num = int(input('Second number:'))

if fi_num > sec_num:
    print(sec_num,'\r',fi_num)
else:
    print(fi_num,'\r',sec_num)


'''
Author's solution:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
'''

