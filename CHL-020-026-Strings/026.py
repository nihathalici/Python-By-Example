'''
Pig Latin takes the first consonant of a word, moves it to the end of the word
and adds on an “ay”. If a word begins with a vowel you just add “way” to the
end. For example, pig becomes igpay, banana becomes ananabay, and aadvark
becomes aadvarkway. Create a program that will ask the user to enter a word
and change it into Pig Latin. Make sure the new word is displayed in lower case.
'''

consonants = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z'
	
vowels = 'a, e , i, o, u]

word = input('Enter a word: ')

pigged_word= ''
if word[:1] in consonants:
    pigged_word = word[1:] + word[:1] + 'ay'
elif word[:1] in vowels:
    pigged_word = word + 'way' 

print(pigged_word)

'''
Author's solution:

word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1: length]
if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
    newword = rest + first + 'ay'
else:
    newword = word + 'way'
print(newword.lower())
'''



