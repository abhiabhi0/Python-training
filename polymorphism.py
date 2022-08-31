# Python program to demonstrate in-built poly-
# morphic functions
 
# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))

###############################

# Examples of user-defined polymorphic functions : 

def add(x, y, z = 0):
    return x + y+z
 
# Driver code
print(add(2, 3))
print(add(2, 3, 4))

####################################

# Polymorphism with class methods: 


class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# Polymorphism with Inheritance: 
# Method Overriding

from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am a two-dimensional shape."
    def __str__(self):
        return self.name
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2
shape_circle = Circle(7)
print(shape_circle)
print(shape_circle.area())
print(shape_circle.fact())

