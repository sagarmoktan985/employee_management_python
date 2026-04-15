#SAGAR_MOKTAN_TAMANG, SAROJ_SHRESTHA, BASANTA_SHRESTHA, UJJWAL_SHRESTHA
# NPO71219, NP071343, NP071293, NP071311

from functions import add_employee, view_employees, delete_employee, view_enquiry, edit_employee_profile, employee_reset_password
# EMPLOYEE LOGIN
def employee_login():
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ").strip()

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = [x.strip() for x in line.strip().split(",")]

                if len(data) >= 8 and data[6] == email and data[7] == password:
                    print("Login Successful")
                    employee_menu(data)
                    return

        print("Login Failed")

    except FileNotFoundError:
        print("employees.txt file not found")


# EMPLOYEE MENU 

def employee_menu(data):

    while True:

        print("\n--- Employee Menu ---")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Send Suggestion")
        print("4. Send Enquiry")
        print("5. Reset Password: ")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nYour Profile")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Designation:", data[2])
            print("Age:", data[3])
            print("Address:", data[4])
            print("Salary:", data[5])
            print("Email:", data[6])

        elif choice == "3":

            suggestion = input("Enter suggestion: ")

            file = open("suggestion.txt", "a")
            file.write(data[1] + ": " + suggestion + "\n")
            file.close()

            print("Suggestion sent")

        elif choice == "4":

            enquiry = input("Enter enquiry: ")

            file = open("enquiry.txt", "a")
            file.write(data[1] + ": " + enquiry + "\n")
            file.close()

            print("Enquiry sent")
        elif choice == "2":
            edit_employee_profile(data)

        elif choice == "5":
            employee_reset_password(data)

        elif choice == "6":
            break
        

        
    
