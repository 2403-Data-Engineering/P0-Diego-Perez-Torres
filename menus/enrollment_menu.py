def display_enrollment_menu():
    print("~~~~~~~~~~Enrollment Menu~~~~~~~~~~")
    print("1. Enroll a student to a class")
    print("2. Drop a student from a class")
    print("3. View all students in a specific class")
    print("0. Go back to previous menu")

def class_menu():
    while True:
        display_enrollment_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            print("not implemented")
        elif choice == '2':
            print("not implemented")
        elif choice == '3':
            print("not implemented")
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")