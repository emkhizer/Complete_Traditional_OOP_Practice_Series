"""
    9. Abstract Classes and Methods Assignment:
    Use the abc module to create an abstract class Shape with an abstract method area(). 
    Inherit a class Rectangle that implements area().
"""

from abc import ABC, abstractmethod  # Abstract class banane ke liye ye module use hota hai

# Abstract class Shape
class Shape(ABC):  # ABC ka matlab Abstract Base Class
    @abstractmethod
    def area(self):
        # Yeh ek abstract method hai — iska koi body nahi hai
        # Isse subclass me implement karna zaroori hota hai
        pass


# Rectangle class, Shape se inherit kar rahi hai
class Rectangle(Shape):
    def __init__(self, width, height):
        # Constructor width aur height set karega
        self.width = width
        self.height = height

    def area(self):
        # Yeh abstract method ka actual implementation hai
        return self.width * self.height  # Rectangle ka area: width × height


# Example usage
if __name__ == "__main__":
    rect = Rectangle(5, 10)  # Rectangle object bana rahe hain

    print("Area of rectangle:", rect.area())  # Area print karega: 50

"""
from abc import ABC, abstractmethod
➤ Yeh import zaroori hota hai abstract class aur method banane ke liye.

class Shape(ABC):
➤ Shape ek abstract class hai, jo ABC (Abstract Base Class) se inherit kar rahi hai.

@abstractmethod def area(self):
➤ Yeh method sirf declare kiya gaya hai — body nahi hai. Iska matlab hai ke har subclass ko iska apna version likhna hoga.

class Rectangle(Shape):
➤ Rectangle class Shape ko inherit karti hai, aur area() method ko implement karti hai.

def area(self): return self.width * self.height
➤ Yeh actual logic hai area calculate karne ka, jo abstract method ka complete version hai.
"""