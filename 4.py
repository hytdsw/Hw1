class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата: {self.salary} грн."

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        self.employees = [emp for emp in self.employees if emp.name != employee_name]

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)

    def list_employees(self):
        if not self.employees:
            print(f"Відділ '{self.name}' порожній.")
        else:
            print(f"Співробітники відділу '{self.name}':")
            for employee in self.employees:
                print(employee)

# Приклад використання
department = Department("IT")

# Додаємо співробітників
employee1 = Employee("Олексій", "Програміст", 30000)
employee2 = Employee("Марія", "Тестувальник", 20000)

department.add_employee(employee1)
department.add_employee(employee2)

# Виводимо список співробітників
department.list_employees()

# Підраховуємо загальну зарплату
total_salary = department.calculate_total_salary()
print(f"\nЗагальна зарплата відділу: {total_salary} грн")

# Видаляємо співробітника
department.remove_employee("Марія")

# Оновлений список співробітників
print("\nОновлений список співробітників:")
department.list_employees()
