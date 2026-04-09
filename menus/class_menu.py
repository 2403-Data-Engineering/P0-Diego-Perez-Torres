import database.db_class_manager as dbc

def delete_class():
    while True:
        #add testing for existing/non-existing ids
        try:
            class_id_choice = int(input("Please enter a valid class ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        delete_choice = input("Are you sure you want to delete this class? y/n : ")
        if delete_choice == 'y':
            dbc.delete_class_by_id(class_id_choice)
            print("Class deleted.")
        elif delete_choice == 'n':
            print("Deletion cancelled. \n")
        else:
            print("Invalid choice, please enter either y or n. \n")
        break

def update_class_data(id: int):
    class_name = input("What is the class's name?: ").strip()
    professor_id = input("What is the professor's ID?: ").strip()
    dbc.update_class_by_id(id,class_name,professor_id)

def update_class():
    while True:
        #add testing for existing/non-existing ids
        try:
            class_id_choice = int(input("Please enter a valid class ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        update_class_data(class_id_choice)
        break 

def view_classes():
    dbc.view_all_classes()

def create_class():
    class_name = input("What is the class's name?: ").strip()
    professor_id = input("What is the professor's ID?: ").strip()
    dbc.insert_professor(class_name,professor_id)

def display_class_menu():
    print("~~~~~~~~~~Class Menu~~~~~~~~~~")
    print("1. Create a new class")
    print("2. View all classes")
    print("3. Update a class's details")
    print("4. Delete a class")
    print("0. Go back to previous menu")

def class_menu():
    while True:
        display_class_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            create_class()
        elif choice == '2':
            view_classes()
        elif choice == '3':
            update_class()
        elif choice == '4':
            delete_class() 
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")