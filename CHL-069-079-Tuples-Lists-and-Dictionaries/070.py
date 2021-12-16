'''
Add to program 069 to ask the user to enter a number
and display the country in that position.
'''

cnt_tpl = ('Island', 'Norway', 'Sweden', 'Denmark', 'Finland')

num = int(input('Enter index number: '))

print('{} has the index number: {}'.format( cnt_tpl[num], num  ) )
