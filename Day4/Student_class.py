class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"Student name:{self.name}\nroll.no:{self.rollno}\nmarks:{self.marks}")
s1=Student("alice",10,98)
s2=Student("bob",12,95)
s1.display()
s2.display()