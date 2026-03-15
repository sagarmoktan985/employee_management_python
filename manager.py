from functions import add_employee, view_employees, delete_employee, view_enquiry, reset_manager_password, edit_manager_profile, search_employees

# MANAGER LOGIN
def manager_login():
    email = input("Enter Manager Email: ")
    password = input("Enter Password: ")

    try:
        file = open("managers.txt", "r")

        for line in file:
            data = line.strip().split(",")
            if data[2] == email and data[3] == password:
                print("Manager Login Successful")
                manager_menu(data)
                return

        print("Login Failed")

    except FileNotFoundError:
        print("Manager file not found")


# MANAGER MENU
def manager_menu(manager_data):
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. View Enquiry")
        print("5. Reset Manager Password")
        print("6. Edit My Profile")
        print("7. Search Employees")
        print("8. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            delete_employee()

        elif choice == "4":
            view_enquiry()

        elif choice == "5":
            manager_data = reset_manager_password(manager_data)

        elif choice == "6":
            manager_data = edit_manager_profile(manager_data)
        elif choice == "7":
            search_employees()
        elif choice == "8":
            break

        else:
            print("Invalid choice")

def reset_manager_password():

    email = input("Enter your manager email: ")
    new_password = input("Enter new password: ")

    try:
        file = open("managers.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("managers.txt", "w")

        for line in lines:
            data = line.strip().split(",")

            if data[2] == email:
                data[3] = new_password
                print("Password updated successfully")

            file.write(",".join(data) + "\n")

        file.close()

    except FileNotFoundError:
        print("Manager file not found")