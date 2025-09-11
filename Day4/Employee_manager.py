class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee details:")
        print(f"Employee name:{self.name}\nEmployee salary:{self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        print("Manager details:")
        print(f"Manager name:{self.name}\nManager salary:{self.salary}\nManager department:{self.department}")
e=Employee("Alice",70000)
e.display()
m=Manager("Bob",85000,"Data scientist")
m.display()