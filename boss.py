from functions import edit_boss_profile, add_employee, add_manager, view_employees, view_managers, search_employee_manager, delete_employee, delete_manager

# BOSS LOGIN

def boss_login():
    username = "boss"
    password = "123"

    for i in range(3):
        u = input("Enter Boss Username: ")
        p = input("Enter Password: ")

        if u.lower() == username and p == password:
            print("Boss Login Successful")
            boss_menu()
            return
        else:
            print("Wrong login")

    print("3 attempts failed. System closed.")


# BOSS MENU

def boss_menu():
    while True:
        print("\n--- Boss Menu ---")
        print("1. Edit Profile")
        print("2. Add Employee")
        print("3. Add Manager")
        print("4. View Employees")
        print("5. View Managers")
        print("6. Search")
        print("7. Delete Employee")
        print("8. Delete Manager")
        print("9. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            edit_boss_profile()

        elif choice == "2":
            add_employee()

        elif choice == "3":
            add_manager()

        elif choice == "4":
            view_employees()

        elif choice == "5":
            view_managers()

        elif choice == "6":
            search_employee_manager()

        elif choice == "7":
            delete_employee()

        elif choice == "8":
            delete_manager()

        elif choice == "9":
            break

        else:
            print("Invalid choice")
