# BOSS EDIT PROFILE
def edit_boss_profile():

    print("\n--- Edit Boss Profile ---")

    new_username = input("Enter New Username: ")
    new_password = input("Enter New Password: ")

    print("Profile Updated Successfully")

    print("\nUpdated Profile")
    print("Username:", new_username)
    print("Password:", new_password)





#  ADD Manager 
def add_manager():
    id = input("Enter Manager ID: ")
    name = input("Enter Manager Name: ")
    email = input("Enter Manager Email: ")
    password = input("Enter Password: ")

    file = open("managers.txt", "a")
    file.write(f"{id},{name},{email},{password}\n")
    file.close()

    print("Manager added successfully")


   # Manager edit own profile
def edit_manager_profile(manager_data):
    old_email = manager_data[2]

    print("\n--- Edit Manager Profile ---")
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")

    try:
        file = open("managers.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("managers.txt", "w")

        for line in lines:
            data = line.strip().split(",")

            if data[2] == old_email:
                data[1] = new_name
                data[2] = new_email
                manager_data = data
                print("Profile updated successfully")

            file.write(",".join(data) + "\n")

        file.close()
        return manager_data

    except FileNotFoundError:
        print("Manager file not found")
        return manager_data

# RESET MANAGER PASSWORD

def reset_manager_password():
    email = input("Enter Manager Email: ")
    new_password = input("Enter New Password: ")

    try:
        file = open("managers.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("managers.txt", "w")
        found = False

        for line in lines:
            data = line.strip().split(",")

            if len(data) >= 4 and data[2] == email:
                data[3] = new_password
                file.write(",".join(data) + "\n")
                found = True
            else:
                file.write(line)

        file.close()

        if found:
            print("Manager password reset successfully")
        else:
            print("Manager not found")

    except FileNotFoundError:
        print("Manager file not found")

# RESET PASSWORD EMPLOYEE
def employee_reset_password(data):
    new_password = input("Enter new password: ")
    
    try:
        file = open("employees.txt", "r")
        lines = file.readlines()
        file.close()
        
        file = open("employees.txt","w")
        
        for line in lines:
            emp = line.strip().split(",")
            
            if emp[6] == data[6]:
                emp[7] = new_password
                print("Your password has been reset successfully.")
                
            file.write(",".join(emp)+"\n")
            
        file.close()
        
    except FileNotFoundError:
        print("employees.txt file not found.")

#  VIEW managers 
def view_managers():

    try:
        file = open("managers.txt", "r")
        
        print("\nHere is the list Manager: ")
        for line in file:
            print(line.strip())

        file.close()

    except:
        print("No managers found")


# DELETE Manager 

def delete_manager():
    manager_id = input("Enter Manager ID to delete: ")

    try:
        with open("managers.txt", "r") as file:
            lines = file.readlines()

        found = False  # Track if manager exists

        with open("managers.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] != manager_id:
                    file.write(line)
                else:
                    found = True  # Manager matched, so we skip writing

        if found:
            print("Manager deleted successfully.")
        else:
            print("Manager ID not found.")

    except FileNotFoundError:
        print("managers.txt file not found.")


#  ADD EMPLOYEE 

def add_employee():
    id = input("ID: ")
    name = input("Name: ")
    designation = input("Designation: ")
    age = input("Age: ")
    address = input("Address: ")
    salary = input("Salary: ")
    email = input("Email: ")
    password = input("Password: ")

    file = open("employees.txt", "a")
    file.write(f"{id},{name},{designation},{age},{address},{salary},{email},{password}\n")
    file.close()

    print("Employee Added Successfully")

#Employee edit own profile

def edit_employee_profile(employee_data):
    old_email = employee_data[6]

    print("\n--- Edit Employee Profile ---")
    new_name = input("Enter new name: ").strip()
    new_designation = input("Enter new designation: ").strip()
    new_age = input("Enter new age: ").strip()
    new_address = input("Enter new address: ").strip()
    new_email = input("Enter new email: ").strip()

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        with open("employees.txt", "w") as file:
            for line in lines:
                data = [x.strip() for x in line.strip().split(",")]

                if len(data) >= 8 and data[6] == old_email:
                    data[1] = new_name
                    data[2] = new_designation
                    data[3] = new_age
                    data[4] = new_address
                    data[6] = new_email
                    employee_data = data

                file.write(",".join(data) + "\n")

        print("Employee profile updated successfully")
        return employee_data

    except FileNotFoundError:
        print("employees.txt file not found")
        return employee_data



#  VIEW EMPLOYEES 

def view_employees():
    try:
        file = open("employees.txt", "r")
        data = file.readlines()
        file.close()

        if not data:  # file is empty
            print("No employees found.")
            return
        
        print("\nHere is the list Employees: ")
        for line in data:
            line = line.strip()
            if line:  # only print non-empty lines
                print(line)

    except FileNotFoundError:
        print("employees.txt file not found.")


#  DELETE EMPLOYEE 

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        found = False  # Track if employee exists

        with open("employees.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] != emp_id:
                    file.write(line)
                else:
                    found = True  # Employee matched, so skip writing

        if found:
            print("Employee deleted successfully.")
        else:
            print("Employee ID not found.")

    except FileNotFoundError:
        print("employees.txt file not found.")



# Search Employee and Mangers.
def search_employee_manager():
    choice = input("Enter 1 to search Employee or Enter 2 to search Manager: ")

    if choice == "1":
        print("\nYou chose 1 ,so you are able to search employee.")
        keyword = input("Enter Employee ID/ Name/ Email to search: ")
        try:
            with open("employees.txt", "r") as file:
                for line in file:
                    if keyword in line:
                        print(line.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("employees.txt file not found.")

    elif choice == "2":
        print("\nYou chose 2 ,so you are able to search manager.")
        keyword  = input("Enter Manager ID/ Name/ Email to search: ")
        try:
            with open("managers.txt", "r") as file:
                for line in file:
                    if keyword in line:
                        print(line.strip())
                        return
            print("Manager not found.")
        except FileNotFoundError:
            print("managers.txt file not found.")

    else:
        print("Invalid choice. Please enter 1 or 2.")


# Search Employee from  Mangers.

def search_employees():

    keyword = input("Enter Name / ID / Email: ")

    print("\nEmployees Found:")
    file = open("employees.txt","r")
    for line in file:
        if keyword in line:
            print(line.strip())
    file.close()

# VIEW ENQUIRY 

def view_enquiry():

    try:
        file = open("enquiry.txt", "r")

        for line in file:
            print(line.strip())

        file.close()

    except:
        print("No enquiry found")
