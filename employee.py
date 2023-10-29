from calendar import weekday
from multiprocessing import Manager


class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    # Dunder special methods start with double underscores
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        #self.email = f'{first_name}.{last_name}@company.com'
        Employee.number_of_employees += 1

    def __repr__(self):
        return f'Employee({self.first_name}, {self.last_name}, {self.pay})'

    def __str__(self):
        return f'{self.full_name()} - {self.email}'

    # Using decorator class method to create alternative constructor to create emplyees from string
    @classmethod
    def from_string(cls, employee_str):
        first, last, pay = employee_str.split('-')
        return cls(first, last, pay)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first_name = None
        self.last_name = None

    # Adding property decorator to mether so email can be access as attibute vs. function/method

    @property
    def email(self):
        return f'{self.first_name}@{self.last_name}@email.com'


    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Static methods does use self
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Inheritance
# Lets create different type of employees
# Employee -> Developer
#          -> Manager
# use the help function to visualize inheritance chain -> help(Developer)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self. employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'--> {emp.full_name()}')



emp_1 = Employee('Mariusz', 'Kolodziej', '100000')

emp_1.first_name = 'Bob'

emp_1.fullname = 'Mariusz Kolodziej'

del emp_1.fullname

print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.email)
print(emp_1.fullname)



# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())


# dev_1 = Developer('Mariusz', 'Kolodziej', '100000', 'Python')
# dev_2 = Developer('Ursula', 'Tracz', '200000', 'Java')

# mgr_1 = Manager('Bob', 'Smith', '90000', [dev_1])
# mgr_1.add_emp(dev_2)
# print(mgr_1.email)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)


# print(help(Developer))
# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)
# print(employee_2.email)
# import datetime
# my_date = datetime.date(2022, 7, 11)
# print(Employee.is_workday(my_date))
# print(employee_1.full_name())
# print(employee_2.full_name())
# print(employee_1.raise_amount)
# print(Employee.raise_amount)
# print(employee_1.__dict__)
# print(Employee.__dict__)
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)