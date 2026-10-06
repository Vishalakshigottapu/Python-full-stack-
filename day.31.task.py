#students marks file manager
with open("marks.txt", "w") as file:
    for i in range(5):
        try:
            mark = int(input("Enter student mark: "))
            if mark >= 0 and mark <= 100:
                file.write(str(mark) + "\n")
                print("Mark saved successfully")
            else:
                print("Invalid mark")
        except ValueError:
            print("Invalid mark")
print("\nSaved Marks:")
with open("marks.txt", "r") as file:
    for mark in file:
        print(mark.strip())
        
#Expense tracker
with open("expenses.txt", "w") as file:
    for i in range(5):
        try:
            expense = float(input("Enter expense: "))
            if expense > 0:
                file.write(str(expense) + "\n")
            else:
                print("Invalid expense")
        except ValueError:
            print("Invalid expense. Please enter a number.")
print("\nExpenses:")
total = 0
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            expense = float(line)
            print(expense)
            total = total + expense
    print("Total expense:", total)
except FileNotFoundError:
    print("File not found")
    
#student attendance manager
with open("attendance.txt", "w") as file:
    for i in range(5):
        try:
            name = input("Enter student name: ")
            status = input("Enter attendance (P/A): ").upper()
            if status == "P" or status == "A":
                file.write(name + "," + status + "\n")
            else:
                print("Invalid attendance status")
        except:
            print("Invalid input")
print("\nPresent Students:")
try:
    with open("attendance.txt", "r") as file:
        for line in file:
            name, status = line.strip().split(",")
            if status == "P":
                print(name)
except FileNotFoundError:
    print("File not found")
