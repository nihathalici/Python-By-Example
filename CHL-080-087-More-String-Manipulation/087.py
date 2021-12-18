'''
Ask the user to type in a word and then display it
backwards on separate line.
'''


word = input("Enter a word: ")

length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
