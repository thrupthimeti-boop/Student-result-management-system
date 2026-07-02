import csv

print("====================================")
print("Student Result Management System")
print("====================================")

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

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
        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        search_id = input("Enter Student ID to search: ")
        found = False

        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == search_id:
                        print("\nStudent Found")
                        print("ID:", row[0])
                        print("Name:", row[1])
                        print("Marks:", row[2])
                        found = True
                        break

            if not found:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "4":
        update_id = input("Enter Student ID to update: ")
        updated_rows = []
        found = False

        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == update_id:
                        new_name = input("Enter New Name: ")
                        new_marks = input("Enter New Marks: ")
                        updated_rows.append([update_id, new_name, new_marks])
                        found = True
                    else:
                        updated_rows.append(row)

            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Student record updated successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "5":
        delete_id = input("Enter Student ID to delete: ")
        updated_rows = []
        found = False

        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == delete_id:
                        found = True
                    else:
                        updated_rows.append(row)

            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
