'''
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
'''


file = open("Names.txt", "w")
file.write('John\nJames\nMary\nSophie\nTom')
file.close()

"""
Author's solution:

file = open("Names.txt", "w")
file.write("Bob\n")
file.write("Tom\n")
file.write("Gemma\n")
file.write("Sarah\n")
file.write("Timothy\n")
file.close()
"""
