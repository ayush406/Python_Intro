from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self . length = 6
        self.breadth = 8

    def printarea(self):
        return self.length * self.breadth

# if we derive a class which has abstract methods, then its mandatory to define that method inside the base class.

square = Rectangle()
# we can't create object from abstract class shape.
print(square.printarea())
