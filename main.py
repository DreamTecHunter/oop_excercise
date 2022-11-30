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


class HeadOfGroup(Employee):
    def __init__(self, first_name: str, last_name: str, sex: Sex, department: Department = None):
        super().__init__(first_name, last_name, sex, department)


class Company:
    def __init__(self, employees: list = None):
        self.employees = [] if employees is None else employees

    def count_employees_via_type(self, employee_type: type):
        return len([e for e in self.employees if type(e) == employee_type])

    def count_departments(self):
        return len({e.department for e in self.employees})

    def count_employees_per_department(self):
        departments = {e.department: 0 for e in self.employees}
        for e in self.employees:
            departments[e.department] += 1
        return departments

    def get_biggest_department(self):
        biggest_department = list(self.count_employees_per_department().keys())[0]
        for key in self.count_employees_per_department().keys():
            biggest_department = key if self.count_employees_per_department()[key] > \
                                        self.count_employees_per_department()[
                                            biggest_department] else biggest_department
        return biggest_department

    def get_sex_ration(self):
        counter = {
            Sex.MALE: 0,
            Sex.FEMALE: 0
        }
        for employee in self.employees:
            counter[employee.sex] += 1 / len(self.employees)
        return counter


if __name__ == '__main__':
    company = Company([
        Employee("a", "a", Sex.MALE, Department.UNDEFINED),
        HeadOfGroup("a", "a", Sex.MALE, Department.MARKETING),
        HeadOfGroup("a", "b", Sex.MALE, Department.MARKETING)
    ])
    print(company.count_employees_via_type(Employee))
    print(company.count_departments())
    print(company.get_biggest_department())
    print(company.get_sex_ration())
