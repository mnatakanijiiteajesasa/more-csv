print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file \n")
user_choice = input("Make a selection 1, 2 or 3:")

if user_choice == "1":
    subject = input("What is your favourite subject? \n")
    file = open("Subject.txt", "w")
    file.write(subject)
    file.close()
elif user_choice == "2":
    file = open("Subject.txt", "r")
    print(file.read())
elif user_choice == "3":
    new_subject = input("Enter a new subject: \n")
    file = open("Subject.txt", "a")
    file.write(new_subject)
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Sorry! Invalid Choice")