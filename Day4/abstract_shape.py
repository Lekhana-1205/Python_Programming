from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print("Area of rectangle:",ar)
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        ar=pi*self.radius*self.radius
        print("Area of circle:",ar)
r=Rectangle(4,5)
r.area()
c=Circle(7)
c.area()