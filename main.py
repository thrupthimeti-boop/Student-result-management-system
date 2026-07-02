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

        while True:
            math = int(input("Enter Math Marks (0-100): "))
            if 0 <= math <= 100:
                break
            print("Invalid marks! Enter between 0 and 100.")

        while True:
            science = int(input("Enter Science Marks (0-100): "))
            if 0 <= science <= 100:
                break
            print("Invalid marks! Enter between 0 and 100.")

        while True:
            english = int(input("Enter English Marks (0-100): "))
            if 0 <= english <= 100:
                break
            print("Invalid marks! Enter between 0 and 100.")

        total = math + science + english
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                student_id,
                student_name,
                math,
                science,
                english,
                total,
                percentage,
                grade
            ])

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                print("\nStudent Records")
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
                        print("Math:", row[2])
                        print("Science:", row[3])
                        print("English:", row[4])
                        print("Total:", row[5])
                        print("Percentage:", row[6])
                        print("Grade:", row[7])
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

                        while True:
                            math = int(input("Enter New Math Marks (0-100): "))
                            if 0 <= math <= 100:
                                break
                            print("Invalid marks!")

                        while True:
                            science = int(input("Enter New Science Marks (0-100): "))
                            if 0 <= science <= 100:
                                break
                            print("Invalid marks!")

                        while True:
                            english = int(input("Enter New English Marks (0-100): "))
                            if 0 <= english <= 100:
                                break
                            print("Invalid marks!")

                        total = math + science + english
                        percentage = total / 3

                        if percentage >= 90:
                            grade = "A"
                        elif percentage >= 80:
                            grade = "B"
                        elif percentage >= 70:
                            grade = "C"
                        elif percentage >= 60:
                            grade = "D"
                        else:
                            grade = "F"

                        updated_rows.append([
                            update_id,
                            new_name,
                            math,
                            science,
                            english,
                            total,
                            percentage,
                            grade
                        ])
                        found = True

                    else:
                        updated_rows.append(row)

            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Student updated successfully!")
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
