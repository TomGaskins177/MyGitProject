FILE_NAME = "students.txt"

# input validation functions

# ensures input is not blank
def validate_name(name):
    if name == "":
        return False
    return True

def validate_grade(grade):
    try:
        # grade as a whole number
        grade = int(grade)

        # checks to see if grade falls between 0-100
        if grade >= 0 and grade <= 100:
            return True
        else:
            return False
    except:
        return False
    
# file saving function

# saves a student with their name and grade
def save_student(name, grade):
    # opens students.txt file
    file = open (FILE_NAME, "a") # use "a" to append
    # writes in students.txt file
    file.write(name + "," + str(grade) + "\n")
    # closes students.txt file
    file.close()
    print("Student saved successfully.")

# file loading function

# loads all students in students.txt
def load_students():
    try:
        file = open (FILE_NAME, "r")
        print("Student List:")

        for line in file:
            data = line.strip().split(",")
            print("Name:", data[0], "| Grade:", data[1])

        file.close()

    except:
        print("No file found.")
