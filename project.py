# Aphral Griffin
# 29/03/2019
# Modular Programming Project
from myClasses import Employees


# prints menu and gets users choice
def get_choice():
    while True:
        try:
            selection = int(input("\n-----Options----- \n1.View All Employees\n2.View Single Employee\n"
                                  "3.Edit Single Salary\n4.Add New Employee\n5.Delete An Employee\n6.Give Bonus\n"
                                  "7.Generate Report\n8.Quit\nPlease Choose One Of The Above Options: "))
            return selection
        except ValueError:
            print("\nPlease Enter A Number! ")


# depending on users choice calls different functions
def read_choice(employees):
    while True:
        selection = get_choice()
        if selection == 1:
            employees.display_all()
        elif selection == 2:
            employees.display_record()
        elif selection == 3:
            employees.edit_salary()
        elif selection == 4:
            employees.add_employee()
        elif selection == 5:
            employees.delete_employee()
        elif selection == 6:
            employees.bonus_given()
        elif selection == 7:
            employees.create_report()
        elif selection == 8:
            employees.save_quit()
            break
        else:
            print("--- Please Choose An Option Below ---")


def main():
    employees = Employees()
    read_choice(employees)


main()
