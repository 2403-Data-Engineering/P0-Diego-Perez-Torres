import objects.student as student

dummyStudent = student.Student(1,"nerdy","nathan","nerdynathan@school.edu","Computer Science","2030")
students = [dummyStudent]

def delete_student():
    while True:
        #add testing for existing/non-existing ids
        try:
            student_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        
        if student_id_choice < 1 or student_id_choice > len(students):
            print("Not a valid ID.")
            break
        
        delete_choice = input("Are you sure you want to delete this student? y/n : ")
        if delete_choice == 'y':
            del students[student_id_choice-1]
            print("student deleted.")
        elif delete_choice == 'n':
            print("Deletion cancelled. \n")
        else:
            print("Invalid choice, please enter either y or n. \n")
        break

def view_students():
    for i in students:
        #improve readability
        print(vars(i))

def update_student_data(id: int):
    first_name = input("What is the student's first name?: ").strip()
    last_name = input("What is the student's last name?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    email = first_name+last_name+"@school.edu"
    major = input("What is the student's major?: ").strip()
    year = input("What is the student's graduation year?: ").strip()
    newStudent = student.Student(id,first_name,last_name,email, major,year)
    students.append(newStudent)
    
def update_student():
    while True:
        #add testing for existing/non-existing ids
        try:
            student_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        update_student_data(student_id_choice)
        break
    
def create_student():
    first_name = input("What is the student's first name?: ").strip()
    last_name = input("What is the student's last name?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    email = first_name+last_name+"@school.edu"
    major = input("What is the student's major?: ").strip()
    year = input("What is the student's graduation year?: ").strip()
    newStudent = student.Student(len(students)+1,first_name,last_name,email, major,year)
    students.append(newStudent)

def display_student_menu():
    print("~~~~~~~~~~Student Menu~~~~~~~~~~")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Remove a student")
    print("5. View all classes a student is enrolled in")
    print("0. Go back to previous menu")

def student_menu():
    while True:
        display_student_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            create_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("not implemented yet")
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")