class Employee:
    def work(self):
        print("Employee is working.")

class Programmer(Employee):
    def work(self):
        print("Programmer is coding.")

class Designer(Employee):
    def work(self):
        print("Designer is designing.")

employees = [Programmer(), Designer()]
for employee in employees:
    employee.work()
        