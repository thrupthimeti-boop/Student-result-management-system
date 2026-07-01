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
        print("Add Student feature coming next.")
    elif choice == "2":
        print("View Students feature coming next.")
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
