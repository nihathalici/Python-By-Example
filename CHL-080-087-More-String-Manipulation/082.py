'''
Show the user a line of text from your favourite poem and ask for a starting
and ending point. Display the characters between those two points.
'''
poem = "When they had sworn to this advised doom"
print(poem)
st_pt = int(input("Enter your starting point: "))
en_pt = int(input("Enter your ending point: "))

print(poem[st_pt:en_pt])
