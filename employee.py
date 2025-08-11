# We are creating this class to create a format of the employee details

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# Lets inherit the class to reuse

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = int(salary)

    def calculate_paycheck(self):
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate