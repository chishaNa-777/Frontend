import json
students = []
next_id = 1


def calculateGrade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C+"
    elif marks >= 40:
        return "C"
    else:
        return "failed"

def Savestudents():
    with open('students.json', 'w') as file:
        json.dump(students, file)

def Loadstudents():
    global students, next_id
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)

        if students:
            numbers = [int(student["id"][3:]) for student in students]
            next_id = max(numbers) + 1
    except FileNotFoundError:
        students = []
        next_id = 1

#===== ADD STUDENTS ========
def getname():
    while True:
        name = input("Enter your name: ")
        if name != "":
            return name
        else:
            print("Please enter a name.")
def getemail():
    while True:
        email = input("Enter email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("Please enter an email.")
def getmarks():
    while True:
        try:
            marks = int(input("Enter student marks: "))
            if marks >=0 and marks <=100:
                return marks
            else:
                print("Please enter a number between 0 and 100")

        except ValueError:
                print("Please enter a number between 0 and 100")

def Addstudent ():
    global next_id
    name = getname()
    email = getemail()
    marks = getmarks()

    grade = calculateGrade(marks)
    student_id = f"STU{next_id:03d}"

    student = {
        "id": student_id,
        "name": name,
        "email": email,
        "marks": marks,
        "grade": grade,
    }
    students.append(student)
    next_id += 1
    Savestudents()

    print("\nStudent added successfully")
    print("student id: ", student_id)
def viewStudents():
    if len(students) == 0:
        print("\nNo students added")
        return
    print("===== student records =====")
    for student in students:
        print("===================")
        print("Student Number: ", student["id"])
        print("Name: ", student["name"])
        print("Email: ", student["email"])
        print("Marks: ", student["marks"])
        print("Grade: ", student["grade"])

def searchStudent():
    search_id = input("Enter student ID: ")
    for student in students:
        if student["id"] == search_id:
          print("Student found")
          print("Student ID: ", student["id"])
          print("name:",student["name"])
          print("email:",student["email"])
          print("marks:",student["marks"])
          print("grade:",student["grade"])
          return

    print("student not found.")

def Savestudents ():
    with open('students.json', 'w') as file:
        json.dump(students, file)

def updatestudent ():
    update_id = input("Enter student ID: ")
    for student in students:
        if student["id"] == update_id:
            print("What do you want to update?")
            print("1: name")
            print("2: email")
            print("3: marks")

            choice = input("Enter your choice: ")
            if choice == "1":
                new_name = input("Enter new name: ")
                student["name"] = new_name
            elif choice == "2":
                new_email = input("Enter new email: ")
                student["email"] = new_email
            elif choice == "3":
                new_marks = getmarks()
                student["marks"] = new_marks
                student["grade"] = calculateGrade(new_marks)
            else:
                print("invalid choice")
                return

            Savestudents ()
            print("Student updated successfully")
            return
    print("student not found.")

def deletestudent ():
    deletestudent_id = input("Enter student ID: ")
    for student in students:
        if student["id"] == deletestudent_id:
            students.remove(student)
            print("student deleted successfully")
            return
    print("student not found.")


Loadstudents()
while True:
    print("\n============ WELCOME TO CHISHA'S STUDENT MANAGEMENT SYSTEM ============")
    print("1: Login")
    print("2: create account")
    print("3: Add student ")
    print("4: view student")
    print("5: Search student")
    print("6: Update student")
    print("7: Delete student")
    print("8: exit the program")

    choice = input("enter your choice: ")

    if choice == "1":
        print("Login")

    elif choice == "2":
        print("Create account")

    elif choice == "3":
        Addstudent()

    elif choice == "4":
        viewStudents()
    elif choice == "5":
        searchStudent()
    elif choice == "6":
        updatestudent()
    elif choice == "7":
        deletestudent()
    elif choice == "8":
        print("Exiting the program")
        break
    else:
        print("Invalid choice")



