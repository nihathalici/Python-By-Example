'''
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.
'''

import csv
import random

score = 0
name = input("What is your name: ")
q1_num1 = random.randint(10, 50)
q1_num2 = random.randint(10, 50)
question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
ans1 = int(input(question1))
realans1 = q1_num1 + q1_num2
if ans1 == realans1:
    score = score + 1

q2_num1 = random.randint(10, 50)
q2_num2 = random.randint(10, 50)
question2 = str(q2_num1) + " + " + str(q2_num2) + " = "
ans2 = int(input(question2))
realans2 = q2_num1 + q2_num2
if ans2 == realans2:
    score = score + 1

file = open("QuizScore.csv", "a")
newrecord = name + "," + question1 + str(ans1) + "," + question2 + str(ans2) + "," + str(score) + "\n"
file.write(str(newrecord))

file.close()
