'''
AS-026
Pig Latin takes the first consonant of a word, moves it to the end of the word
and adds on an “ay”. If a word begins with a vowel you just add “way” to the
end. For example, pig becomes igpay, banana becomes ananabay, and aadvark
becomes aadvarkway. Create a program that will ask the user to enter a word
and change it into Pig Latin. Make sure the new word is displayed in lower case.
'''

#####
# Python By Example
# Exercise 026
# Christopher Hagan
#####

word = input('Enter any word and I will convert it to \'Pig Latin\': ')
if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
    pigLatinWord = word.lower() + 'way'
else:
    pigLatinWord = word[1:len(word)].lower() + word[0].lower() + 'ay'

print('{} in \'Pig Latin\' is {}.'.format(word, pigLatinWord))



