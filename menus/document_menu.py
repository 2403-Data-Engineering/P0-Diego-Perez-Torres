def display_document_menu():
    print("1. Generate a student enrollment form")
    print("2. Generate a professor summary report")
    print("0. Go back to previous menu")

def document_menu():
    while True:
        display_document_menu()
        choice = input("Please enter your choice: ").strip()

        #Was trying to implement it but main couldn't find the directory of anything after a certain point,
        #so a working version was cloned.
        if choice == '1':
            print("not implemented yet")
        elif choice == '2':
            print("not implemented yet")
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")