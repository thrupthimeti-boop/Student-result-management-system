import csv

print("====================================")
print("Student Result Management System")
print("====================================")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, student_name, marks])

        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent Records")
        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
