'''
Ask the user to type in their name and then tell
them how many vowels are in their name.
'''
cnt = 0
vowels = 'a, e, i, o, u'

inp = input("Enter your name: ")

for ch in inp:
    if ch in vowels:
        cnt += 1

print("Your name {} has {} vowels.".format(inp, cnt))
