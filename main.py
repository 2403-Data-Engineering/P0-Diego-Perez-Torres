import menus.student_menu as student_menu
import menus.document_menu as document_menu
import menus.class_menu as class_menu
import menus.professor_menu as professor_menu

def display_main_menu():
    print("~~~~~~~~~~Main Menu~~~~~~~~~~")
    print("1. View the professor menu")
    print("2. View the class menu")
    print("3. View the student menu")
    print("4. View the document generation menu")
    print("0. Exit")


while True:
    display_main_menu()
    choice = input("Please enter your choice: ").strip()
    
    if choice == '1':
        professor_menu.professor_menu()
    elif choice == '2':
        class_menu.class_menu()
    elif choice == '3':
        student_menu.student_menu()
    elif choice == '4':
        document_menu.document_menu()
    elif choice == '0':
        exit_choice = input("Are you sure you want to exit? y/n : ")
        while True:
            if exit_choice == 'y':
                exit(0)
            elif exit_choice == 'n':
                continue
            else:
                print("Invalid choice, please enter either y or n. \n")
    else:
        print("Invalid choice, please enter a valid choice.\n")