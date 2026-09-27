import re

FILE_NAME = "students.txt"


# Validate Email using Regex
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


# Add Student
def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            raise ValueError("Student ID cannot be empty.")

        name = input("Enter Student Name: ").strip()

        if name == "":
            raise ValueError("Student name cannot be empty.")

        age = int(input("Enter Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        email = input("Enter Email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Save student data to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{age},{email}\n")

        print("\nStudent added successfully!")

    except ValueError as e:
        print("\nInvalid Input:", e)

    except Exception as e:
        print("\nAn error occurred:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("\nNo student records found.")
                return

            print("\n========== Student Records ==========")

            for record in records:
                student_id, name, age, email = record.strip().split(",")

                print("Student ID :", student_id)
                print("Name       :", name)
                print("Age        :", age)
                print("Email      :", email)
                print("-------------------------------------")

    except FileNotFoundError:
        print("\nNo student data file found.")

    except Exception as e:
        print("\nAn error occurred:", e)


# Main Program
def main():

    while True:

        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("\nThank you for using Student Record Manager!")
                break

            else:
                print("\nInvalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("\nInvalid input! Please enter a number.")


# Start the program
if __name__ == "__main__":
    main()