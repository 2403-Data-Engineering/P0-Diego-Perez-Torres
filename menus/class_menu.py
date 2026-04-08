import objects.classObj as classObj
dummyClass = classObj.Class(1,"Biology 101","billy bob")
classes = [dummyClass]

def delete_class():
    while True:
        #add testing for existing/non-existing ids
        try:
            class_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        delete_choice = input("Are you sure you want to delete this class? y/n : ")
        if delete_choice == 'y':
            del classes[class_id_choice-1]
            print("Class deleted.")
        elif delete_choice == 'n':
            print("Deletion cancelled. \n")
        else:
            print("Invalid choice, please enter either y or n. \n")
        break

def update_class_data(id: int):
    new_class_name = input("What is the class's name?: ").strip()
    new_professor_name = input("What is the professor's name?: ").strip()
    newClass = classObj.Class(id,new_class_name,new_professor_name)
    classes[id-1] = newClass

def update_class():
    while True:
        #add testing for existing/non-existing ids
        try:
            class_id_choice = int(input("Please enter a valid ID: "))
        except ValueError:
            print("Not a valid ID.")
            break
        
        if class_id_choice < 1 or class_id_choice > len(classes):
            print("Not a valid ID.")
            break
        
        update_class_data(class_id_choice)
        break 

def view_classes():
    for i in classes:
        #improve readability
        print(vars(i))

def create_class():
    class_name = input("What is the class's name?: ").strip()
    professor_name = input("What is the professor's name?: ").strip()
    newClass = classObj.Class(len(classes)+1,class_name,professor_name)
    classes.append(newClass)

def display_class_menu():
    print("~~~~~~~~~~Class Menu~~~~~~~~~~")
    print("1. Create a new class")
    print("2. View all classes")
    print("3. Update a class's details")
    print("4. Delete a class")
    print("5. Enroll a student to a class")
    print("6. Drop a student from a class")
    print("7. View all students in a specific class")
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
        elif choice == '5':
            print("not implemented yet")
        elif choice == '6':
            print("not implemented yet")
        elif choice == '7':
            print("not implemented yet")  
        elif choice == '0':
            return
        else:
            print("Invalid choice, please enter a valid choice.\n")