'''
Create a tuple containing the names of five countries and display the whole tuple.

Ask the user to enter one of the countries that have been shown to them and then
display the index number (i.e. position in the list) of that item in the tuple.
'''

cnt_tpl = ('Island', 'Norway', 'Sweden', 'Denmark', 'Finland')

print(cnt_tpl)

name = input('Enter a country name: ')

print('{} has the index number: {}'.format( name, cnt_tpl.index(name) ) )


