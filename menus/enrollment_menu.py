import database.db_enrollment_manager as dbem

def view_enrolled_classes():
    while True:
        try:
            student_id_choice = int(input("Please enter a valid student ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        dbem.view_enrolled_classes(student_id_choice)
        break

def view_students_in_a_class():
    while True:
        try:
            class_id_choice = int(input("Please enter a valid class ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        dbem.view_students_in_a_class(class_id_choice)
        break 

def drop_student_from_a_class():
    while True:
        try:
            class_id_choice = int(input("Please enter a valid class ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        try:
            student_id_choice = int(input("Please enter a valid student ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        dbem.drop_student_from_a_class(class_id_choice,student_id_choice)
        break 

def enroll_student_to_class():
    while True:
        try:
            class_id_choice = int(input("Please enter a valid class ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        try:
            student_id_choice = int(input("Please enter a valid student ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        dbem.enroll_student_to_class(class_id_choice,student_id_choice)
        break 

def display_enrollment_menu():
    print("~~~~~~~~~~Enrollment Menu~~~~~~~~~~")
    print("1. Enroll a student to a class")
    print("2. Drop a student from a class")
    print("3. View all students in a specific class")
    print("4. View all classes a student is enrolled in")
    print("0. Go back to previous menu")

def enrollment_menu():
    while True:
        display_enrollment_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            enroll_student_to_class()
        elif choice == '2':
            drop_student_from_a_class()
        elif choice == '3':
            view_students_in_a_class()
        elif choice == '4':
            view_enrolled_classes()
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")