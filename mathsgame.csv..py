import csv
import random

score = 0
user_name = input("What is your name? ")
quiz1_num1 = random.randint(10, 50)
quiz1_num2 = random.randint(10, 50)
question1 = str(quiz1_num1) + "+" + str(quiz1_num2) + "="
answer1 = int(input(question1))
real_answer1 = quiz1_num1 + quiz1_num2
if answer1 == real_answer1:
    score = score + 1
quiz2_num1 = random.randint(10, 50)
quiz2_num2 = random.randint(10, 50)
question2 = str(quiz2_num1) + "+" + str(quiz2_num2) + "="

answer2 = int(input(question2))
real_answer2 = quiz2_num1 + quiz2_num2
if answer2 == real_answer2:
    score = score + 1
file = open("QuizScore.csv", "a")
new_record = (user_name + "," + question1 + "," + str(answer1) + "," + question2 + "," + str(answer2) + str(score))
file.write(str(new_record))

file.close()




