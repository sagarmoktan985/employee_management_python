#SAGAR_MOKTAN_TAMANG, SAROJ_SHRESTHA, BASANTA_SHRESTHA, UJJWAL_SHRESTHA
# NPO71219, NP071343, NP071293, NP071311

import boss as b
import manager as m
import employee as e

while True:
    print("\nEmployee Management System ")
    print("1. Boss")
    print("2. Manager")
    print("3. Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        b.boss_login()

    elif choice == "2":
        m.manager_login()

    elif choice == "3":
        e.employee_login()

    elif choice == "4":
        print("System Closed.")
        break

    else:
        print("Invalid choice.")