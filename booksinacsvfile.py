import csv

file = open("Books.csv", "a")
newRecord = "To KIll A Mocking Bad, Harper lee, 1960\n"
file.write(str(newRecord))
newRecord = "A Belief History of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))
newRecord = "The Great Gatsby, F.Scott, 1922\n"
file.write(str(newRecord))
newRecord = "The Man Who Mistook His Wife For a Hat, Oliver Sacks, 1985\n"
file.write(str(newRecord))
newRecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newRecord))
file.close()

file = open("Books.csv", "a")
title = input("Enter a book title: ")
author = input("Enter the name of the author: ")
year = input("Enter the year the book was produced")
new_record = title + "," + author + "," + year + "\n"
file.write(str(new_record))
file.close()

file = open("Books.csv", "r")
for row in file:
   print(row)

nums = int(input("How many numbers do you want to add? "))
file = open("Books.csv", "a")
for x in range(0, nums):
    title = input("Enter a book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year the book was produced: ")
    new_record = title + "," + author + "," + year + "\n"
file.write(str(new_record))
file.close()
search_author = input("Enter the name of the author you are looking for: ")

file = open("Books.csv", "r")
count = 0
for row in file:
   if search_author in row:
       print(row)
       count = count + 1
if count == 0:
   print("That author is not in the list")
file.close()







