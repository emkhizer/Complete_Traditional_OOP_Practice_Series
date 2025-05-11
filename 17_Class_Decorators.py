""" 17. Class Decorators Assignment:
    Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". 
    Apply it to a class Person.
"""
# Class decorator jo greet method add karega
def add_greeting(cls):
    # greet method ko class mein add kar rahe hain
    def greet(self):
        return "Hello from Decorator!"  # Yeh message return karega jab greet() call hoga

    # Greet method ko class ke andar add karna
    cls.greet = greet
    return cls  # Modified class ko return karte hain

# Person class ko decorator ke saath modify karenge
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Person ka naam set karte hain

# Example usage
if __name__ == "__main__":
    person1 = Person("Ali")  # Person object create kar rahe hain
    print(person1.greet())  # greet method ko call karenge

"""
def add_greeting(cls):
➤ Yeh ek class decorator hai jo kisi bhi class ko modify karega. 
cls parameter wo class hota hai jisko decorator ke through pass kiya jata hai.

def greet(self):
➤ Yeh ek method hai jo hum Person class ke andar add kar rahe hain. 
Is method ka kaam hai ek greeting message return karna: "Hello from Decorator!".

cls.greet = greet
➤ Hum greet method ko class ke andar add kar rahe hain, matlab ab har Person object ko greet() method mil jayega.

return cls
➤ Modified class ko return kiya jata hai jisme ab greet() method included hai.

@add_greeting
➤ Yeh syntax decorator ko Person class ke upar apply karta hai. 
Iske baad Person class mein automatically greet() method add ho jata hai.

person1.greet()
➤ Ab jab hum person1.greet() call karenge, toh yeh "Hello from Decorator!" print karega, jo humne greet method mein define kiya hai.

Key Points:
Class decorators ek class ko modify karte hain. 
Yeh behaviour ko add ya modify kar sakte hain bina original class ke code ko change kiye.

Is example mein, humne add_greeting decorator banaya jo greet() method ko Person class mein add karta hai.

kisi bhi class ko aise dynamically modify kar sakte hain, jaise ki humne greet() method ko add kiya.
"""    
