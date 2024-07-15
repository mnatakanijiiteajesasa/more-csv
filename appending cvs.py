import csv
num = int(input("How many books do you want to add to the list?"))
file = open("Books.csv", "a")
for x in range(0,num):
    title = input("Enter a book title: ")
    author = input("Enter author's name: ")
    year = input("Enter the year of publication: ")
    newRecord = title + "," + author + "," + year + "\n"
    file.write(str(newRecord))
file.close()

search_author = input("Enter an author's name to search for: ")

file = open("Books.csv", "r")
count = 0
for row in file:
    if search_author in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There are no books written by that author!")
file.close()


