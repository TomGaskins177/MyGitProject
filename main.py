from file_handler import (
    validate_name,
    validate_grade,
    save_student,
    load_students
)

from grade_calculator import (
    calculate_average,
    find_highest,
    find_lowest,
    assign_letter_grade
)


def menu():
    print("\nStudent Manager")
    print("1. Add Student")
    print("2. Show Statistics")
    print("3. Show Saved Students")
    print("4. Exit")


def main():
    grades = []   # used for statistics

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter student name: ")
            if not validate_name(name):
                print("Name cannot be blank.")
                continue

            grade_input = input("Enter grade (0–100): ")
            if not validate_grade(grade_input):
                print("Invalid grade.")
                continue

            grade = int(grade_input)

            save_student(name, grade)
            grades.append(grade)

        elif choice == "2":
            if len(grades) == 0:
                print("No grades entered yet.")
                continue

            avg = calculate_average(grades)
            hi = find_highest(grades)
            lo = find_lowest(grades)
            letter = assign_letter_grade(avg)

            print("\nStatistics")
            print("Average:", round(avg, 2))
            print("Highest:", hi)
            print("Lowest:", lo)
            print("Letter Grade:", letter)

        elif choice == "3":
            load_students()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
