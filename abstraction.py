from abc import ABC, abstractmethod

class Parent(ABC):
  #common function
  def common_fn(self):
    print('In the common method of Parent')
 @abstractmethod
  def abs_fn(self): #is supposed to have different implementation in child classes 
    pass

class Child1(Parent):
  def abs_fn(self):
    print('In the abstract method of Child1')

class Child2(Parent):
  def abs_fn(self):
    print('In the abstract method of Child2')


##Ex2

from abc import ABC,abstractmethod
 
class Animal(ABC):
 
    #concrete method
    def sleep(self):
        print("I am going to sleep in a while")
 
    @abstractmethod
    def sound(self):
    print("This function is for defining the sound by any animal")
        pass
 
class Snake(Animal):
    def sound(self):
        print("I can hiss")
 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")
