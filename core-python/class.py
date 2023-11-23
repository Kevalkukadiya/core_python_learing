class Employee:
    no_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'yopmail.com'

        Employee.no_of_emps += 1
    
    def apply_raise(self):
        self.pay = int(self.pay * 2)

    def fullname(self):
        return  f"{self.first} {self.last} {self.pay} " 

emp_1 = Employee("Keval", "Kukadiya", 5120)
# emp_2 = Employee("Heena", "Solanki", 0)

print(emp_1.fullname())
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(emp_1.__class__)

print(Employee.no_of_emps)