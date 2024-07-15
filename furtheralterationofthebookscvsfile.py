import csv
file = list(csv.reader(open("Books.csv")))
book_list = []
for row in file:
    book_list.append(row)

x = 0
for row in book_list:
    display = x, book_list[x]
    print(display)
    x = x + 1
getrid = int(input("Enter a row number you would like to remove from the list: "))
del book_list[getrid]

x = 0
for row in book_list:
    display = x, book_list[x]
    print(display)
    x = x + 1
alter = int(input("Enter the row number you would like to alter: "))
x = 0
for row in book_list[alter]:
    display = x, book_list[alter][x]
    print(display)
    x = x + 1

part = int(input("Which part do you want to change? "))
new_data = input("Enter new data: ")
book_list[alter][part] = new_data
print(book_list[alter])

file = open("Books.csv", "w")
x = 0
for row in book_list:
    new_record = book_list[x][0] + "," + book_list[x][1] + "," + book_list[x][2] + "\n"
    file.write(new_record)
    x = x + 1
file.close()


