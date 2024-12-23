class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}: {self.name} ({self.position}, ${self.salary})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        for emp in self.employees:
            print(emp)


class Company:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)

    def add_employee_to_department(self, department_name, employee):
        if department_name in self.departments:
            self.departments[department_name].add_employee(employee)

    def generate_report(self):
        print(f"Report for {self.name}")
        for dept_name, dept in self.departments.items():
            print(f"\nDepartment: {dept_name}")
            dept.list_employees()


# start the program
company = Company("Tech Corp")
company.add_department("Engineering")
company.add_department("HR")
company.add_employee_to_department("Engineering", Employee(101, "abdallah", "Engineer", 60000))
company.add_employee_to_department("HR", Employee(102, "behairy", "HR Manager", 50000))
company.generate_report()
