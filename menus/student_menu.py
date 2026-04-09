import database.db_student_manager as dbs

def delete_student():
    while True:
        try:
            student_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        
        delete_choice = input("Are you sure you want to delete this student? y/n : ")
        if delete_choice == 'y':
            dbs.delete_student_by_id(student_id_choice)
            print("student deleted.")
        elif delete_choice == 'n':
            print("Deletion cancelled. \n")
        else:
            print("Invalid choice, please enter either y or n. \n")
        break

def update_student_data(id: int):
    first_name = input("What is the student's first name?: ").strip()
    last_name = input("What is the student's last name?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    email = first_name+last_name+"@school.edu"
    major = input("What is the student's major?: ").strip()
    year = input("What is the student's graduation year?: ").strip()
    dbs.update_student_by_id(first_name,last_name,email,major,year,id)
    
def update_student():
    while True:
        try:
            student_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        update_student_data(student_id_choice)
        break
    
def view_students():
    dbs.view_all_students()
    
def create_student():
    first_name = input("What is the student's first name?: ").strip()
    last_name = input("What is the student's last name?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    email = first_name+last_name+"@school.edu"
    major = input("What is the student's major?: ").strip()
    year = input("What is the student's graduation year?: ").strip()
    dbs.insert_student(first_name,last_name,email,major,year)
    

def display_student_menu():
    print("~~~~~~~~~~Student Menu~~~~~~~~~~")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Remove a student")
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
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")