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

        print("\nStudent Details")
        print("ID:", student_id)
        print("Name:", student_name)
        print("Marks:", marks)
        print("Student added successfully!")

    elif choice == "2":
        print("View Students feature coming next.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
