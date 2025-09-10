t=()
l=[]
def student(roll,name,marks):
    l.append(roll)
    l.append(name)
    l.append(marks)
    t=tuple(l)

for i in range(5):
    roll=int(input("Enter roll no:"))
    name=input("Enter name:")
    marks=int(input())
    student(roll,name,marks)
