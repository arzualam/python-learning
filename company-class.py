# Import the Employee class from the employee.py file
from employee import Employee, SalaryEmployee, HourlyEmployee

#Create another class for the company which lets us add new employees
class Company:
    def __init__(self):
        self.employees = []

# this is to add employee details
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

# To display the details in right format
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('-------------------')

# Lets define the paycheck
    def pay_employees(self):
        print('Pay employees:')
        for i in self.employees:
            print('Paying Employee:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('---------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Arzu', 'Alam', '50000')
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Iniyal', 'Sudharsan', '25', '30')
    my_company.add_employee(employee2)
    employee3 = HourlyEmployee('Sudharsan', 'Punniyakotti', '40', '15')
    my_company.add_employee(employee3)

##This will just call the employee object when we did not have the display_employees object
    #print(my_company.employees)
##this will display the employee names
    my_company.display_employees()
    my_company.pay_employees()
main()