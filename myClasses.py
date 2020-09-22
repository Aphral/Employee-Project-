# Aphral Griffin
# 29/03/2019
# Modular Programming Project


class Employee:
    def __init__(self, employee_num, first_name, last_name, email, salary):
        self.employee_num = employee_num
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary

    def __str__(self):
        return f"\n---- Employee Information ---- \nEmployee Number: {self.employee_num} \n" \
            f"Name: {self.first_name} {self.last_name} \nEmail: {self.email} \nSalary: {self.salary:.2f}\n"

    # returns employee string that looks like csv file line
    def csv_employee(self):
        return f"{self.employee_num},{self.first_name},{self.last_name},{self.email},{self.salary:.2f}"


class Employees:
    def __init__(self):
        self.max_employee_num = 0
        self.employees = self.read_file()

    # opens file and reads data into list, finds largest employee number for later use
    def read_file(self):
            employees = []
            data_file = open("employee.txt")
            for line in data_file:
                line = line.split(",")
                employee_num = int(line[0])
                first_name = line[1].rstrip()
                last_name = line[2].rstrip()
                email = line[3].rstrip()
                salary = float(line[4])
                employee = Employee(employee_num, first_name, last_name, email, salary)
                employees.append(employee)
                if employee_num > self.max_employee_num:
                    self.max_employee_num = employee_num
            data_file.close()
            return employees

    # Writes list to file
    def write_to_file(self, filename):
        employees_file = open(filename, "w")
        for employee in self.employees:
            print(employee.csv_employee(), end="\n", file=employees_file)
        employees_file.close()

    # displays all employees
    def display_all(self):
        for employee in self.employees:
            print(employee)

    # displays a single employees record
    # Should there be an option to hit a key and exit if you don't know a number
    def display_record(self):
        while True:
            employee_num = self.read_nonnegative_int("Enter Employee Number: ")
            for employee in self.employees:
                if employee_num == employee.employee_num:
                    print(employee)
                    return
            print("That Employee Doesn't Exist")

    # Edits salary of single employee and calls writes to file to update file

    def edit_salary(self):
        while True:
            employee_num = self.read_nonnegative_int("Enter Employee Number: ")
            for employee in self.employees:
                if employee_num == employee.employee_num:
                    while True:
                        new_salary = self.read_nonnegative_float("Enter New Salary:")
                        employee.salary = new_salary
                        return
            print("That Employee Doesn't Exist")

    # Adds new employee to file and calls generate_email and generate_num to create new employee email and number

    def add_employee(self):
        first_name = self.read_nonempty_string("Enter First Name: ", "Please Enter First Name")
        last_name = self.read_nonempty_string("Enter Last Name: ", "Please Enter Last Name")
        salary = self.read_nonnegative_float("Enter Salary: ")
        email = self.generate_email(first_name.lower(), last_name.lower())
        employee_num = self.generate_employee_num()
        new_employee = Employee(employee_num, first_name, last_name, email, salary)
        self.employees.append(new_employee)

    # Generates a  email and calls email_exists to check it is unique if not adds number
    def generate_email(self, fname, lname):
        num = 1
        fname = fname.replace("'", "")
        lname = lname.replace("'", "")
        email = f"{fname}.{lname}@cit.ie"
        while True:
                if self.email_exists(email) is True:
                    email = f"{fname}.{lname}{num}@cit.ie"
                    num = num + 1
                else:
                    return email

    # Generates number and calls num_exists to check it is unique if not adds one.
    def generate_employee_num(self):
        employee_num = self.max_employee_num
        while True:
            if self.num_exists(employee_num) is True:
                employee_num = employee_num + 1
            else:
                return employee_num

    # checks if newly generated email is already in the file returns true or false
    def email_exists(self, email):
        for employee in self.employees:
            if email == employee.email:
                return True
        return False

    # checks if newly generated employee number is already in the file returns true or false
    def num_exists(self, employee_num):
        for employee in self.employees:
            if employee_num == employee.employee_num:
                return True
        return False

    # Deletes Employee
    def delete_employee(self):
        employee_num = self.read_nonnegative_int("Enter Employee Number: ")
        for employee in self.employees:
            if employee_num == employee.employee_num:
                self.employees.remove(employee)
                return
        print("That Employee Doesn't Exist")

    # Creates file with employees and there bonus specified by user.
    def bonus_given(self):
        while True:
            while True:
                file = self.read_nonempty_string("Please Enter File For Bonus To Print To: ", "Please Enter A File Name")
                bonus_given = self.read_nonnegative_float("Please Enter A Bonus To Be Given: ")
                bonus_file = open(file, "w")
                for employee in self.employees:
                    bonus = ((bonus_given / 100) * employee.salary)
                    print(f"Employee Number: {employee.employee_num} \nEmployee Name: {employee.first_name} "
                          f"{employee.last_name} \nBonus: {bonus}\n", file=bonus_file)
                return

    # Creates a report of largest salary, the people who have the largest salary and average salary
    def create_report(self):
        total = 0
        largest_salary = 0
        largest_earners = ""
        file = self.read_nonempty_string("Enter File To Save Report To: ", "Please Enter A File Name")
        report_file = open(file, "w")
        for employee in self.employees:
            if employee.salary > largest_salary:
                largest_salary = employee.salary
                largest_earners = ""
                largest_earners = largest_earners + employee.first_name + " " + employee.last_name + " "
            elif employee.salary == largest_salary:
                largest_earners = largest_earners + "and " + employee.first_name + " " + employee.last_name + " "
            total = total + employee.salary
        avg_salary = total / len(self.employees)
        print(f"Average Salary: {avg_salary:.2f}, \nLargest Salary: {largest_salary:.2f}, "
              f"\nLargest Earner(s): {largest_earners}", file=report_file)
        report_file.close()
        return report_file

    # saves information to employee.txt file and exits program
    def save_quit(self):
        self.write_to_file("employee.txt")

    # Checks Number is not negative or a character
    def read_nonnegative_float(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                if number >= 0:
                    break
                else:
                    print("Non-negative numbers please...")
            except ValueError:
                print("Must Be A Number")
        return number

    # Check string is not empty
    def read_nonempty_string(self, prompt, error):
        while True:
            s = input(prompt)
            s = s.replace(" ", "")
            if len(s) > 0:
                break
            else:
                print(error)
        return s

    # Checks number is not negative or a character and it is an integer
    def read_nonnegative_int(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if number >= 0:
                    break
                else:
                    print("Non-negative numbers please")
            except ValueError:
                print("Must Be A Whole Number")
        return number
