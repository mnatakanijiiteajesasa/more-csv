import csv
# start = int(input("Enter a starting year"))
# end = int(input("Enter an ending year"))
# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#    tmp.append(row)

# x = 0
# for row in tmp:
#    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
#        print(tmp[x])
#    x = x + 1


# displaying rows

file = open("Books.csv", "r")
x = 0
for row in file:
        display = ("Row:" + str(x) + "-" + row)
        print(display)
        x = x + 1
