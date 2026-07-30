# 1. class and object
# Object = Real thing created from Class

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def student(self):
        print("Name:", self.name)
        print("ID:", self.id)

leader = Person("Arun kumar", 12)
leader.student()

# 2 .Encapsulation
# We make variables private so nobody can change them directly.
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def display_info(self):
        print("Name:", self.__name)
        print("Salary:", self.__salary)

emp = Employee("Rohit", 50000)
emp.display_info()

# 3. Inheritance
# All animals can eat. Dog is also an animal.
class Animal:   # Parent class
    def eat(self):
        print("Animal speaks")

class Dog(Animal): # Child class
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()  # Inherited method Parent class
dog.bark() # Child class method

# 4. Polymorphism
# Cow sounds and Cat sounds are different, but the method name is same.
class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")

for animal in (Cat(),Cow()):
    animal.sound()

# 5. Abstraction
# Hiding complex implementation details and showing only the necessary parts.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())


