def display_document_menu():
    print("1. Generate a student enrollment form")
    print("2. Generate a professor summary report")
    print("0. Go back to previous menu")

def document_menu():
    while True:
        display_document_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            print("not implemented yet")
        elif choice == '2':
            print("not implemented yet")
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")