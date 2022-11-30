from enum import Enum


class Department(Enum):
    UNDEFINED = 0
    MANAGEMENT = 1
    MARKETING = 2
    PRODUCTION = 3


class Sex(Enum):
    MALE = 0
    FEMALE = 1


class Person(object):
    def __init__(self, first_name: str, last_name: str, sex: Sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex


class Employee(Person):
    def __init__(self, first_name: str, last_name: str, sex: Sex, department: Department = None):
        super().__init__(first_name, last_name, sex)
        self.department = Department.UNDEFINED if department is None else department


class HeadOfDepartment(Employee):
    def __init__(self, first_name: str, last_name: str, sex: Sex, department: Department = None):
        super().__init__(first_name, last_name, sex, department)


class Company:
    def __init__(self, employees: list = None):
        self.employees = [] if employees is None else employees

    def count_employees_via_type(self, employee_type: type):
        return len([e for e in self.employees if type(e) == employee_type])

    def count_departments(self):
        return


if __name__ == '__main__':
    company = Company([
        Person("a", "a", Sex.MALE),
        Employee("a", "a", Sex.MALE, Department.UNDEFINED),
        HeadOfDepartment("a", "a", Sex.MALE, Department.UNDEFINED)
    ])
    print(company.count_employees_via_type(Employee))
