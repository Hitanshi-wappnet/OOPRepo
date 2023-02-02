import zope.interface
import random

PI=3.14

#define interface class
class Shape(zope.interface.Interface): 
    def area(self):
        pass

#Implementing the interface class
@zope.interface.implementer(Shape)
class Square:
    length=int(input("Enter the length of square"))
    def area(self):  #Calculate area
        print("The area  of the square is",self.length*self.length)

    def Perimeter(self):
        print("The perimeter of the square is ",4*self.length)

class Rectangle:    
    def area(self):   #Calculate area
        self.length=int(input("Enter the length of rectangle"))
        self.breadth=int(input("Enter the breadth of rectangle"))
        print("The area of the rectangle is",self.length*self.breadth)

class Circle:
    def area(self):    #Calculate area
        self.radius=int(input("Enter the radius of the circle"))
        print("The area of the circle is",PI*self.radius*self.radius)

S=Square()
R=Rectangle()
C=Circle()
S.area()
# R.area()
# C.area()
S.Perimeter()