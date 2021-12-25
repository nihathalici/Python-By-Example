'''
Create a .csv file that will store the following data. Call it “Books.csv”.
'''

import csv

file = open("Books.csv", "w")
rec = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(rec)
rec = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(rec)
rec = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(rec)
rec = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(rec)
rec = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(rec)
file.close()

