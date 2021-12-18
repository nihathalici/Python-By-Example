'''
Ask the user to type in their favourite school subject. Display it with
“-” after each letter, e.g. S-p-a-n-i-s-h-.
'''

inp = input("Enter your favourite school subject: ")

for letter in inp:
    print(letter, end='-')
