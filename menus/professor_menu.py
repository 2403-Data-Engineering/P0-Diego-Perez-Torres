import objects.professor as prof
import db_professor_manager as dbp

def delete_professor():
    while True:
        #add testing for existing/non-existing ids
        try:
            professor_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        
        delete_choice = input("Are you sure you want to delete this professor? y/n : ")
        if delete_choice == 'y':
            dbp.delete_professor_by_id(professor_id_choice)
            print("Professor deleted.")
        elif delete_choice == 'n':
            print("Deletion cancelled. \n")
        else:
            print("Invalid choice, please enter either y or n. \n")
        break
        
def update_professor_data(id: int):
    new_first_name = input("What is the professor's first name?: ").strip()
    new_last_name = input("What is the professor's last name?: ").strip()
    new_department = input("What department would they lead?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    new_email = new_first_name+new_last_name+"@school.edu"
    dbp.update_professor_by_id(id,new_first_name,new_last_name,new_department,new_email)

def update_professor():
    while True:
        #add testing for existing/non-existing ids
        try:
            professor_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            continue
        update_professor_data(professor_id_choice)
        break
    
def view_professors():
    dbp.view_all_professors()    
    
def create_professor():
    first_name = input("What is the professor's first name?: ").strip()
    last_name = input("What is the professor's last name?: ").strip()
    department = input("What department would they lead?: ").strip()
    #add a way to check if email already exists, and if so, add numbers
    email = first_name+last_name+"@school.edu"
    dbp.insert_professor(first_name,last_name,department,email)

def display_professor_menu():
    print("~~~~~~~~~~Professor Menu~~~~~~~~~~")
    print("1. Add a professor")
    print("2. View all professors")
    print("3. Update a professor's information")
    print("4. Remove a professor")
    print("0. Go back to previous menu")

def professor_menu():
    while True:
        display_professor_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            create_professor()
        elif choice == '2':
            view_professors()
        elif choice == '3':
            update_professor()
        elif choice == '4':
            delete_professor()
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")