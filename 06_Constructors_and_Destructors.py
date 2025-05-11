"""
    6. Constructors and Destructors Assignment:
    Create a class Logger that prints a message when an object is created 
    (constructor) and another message when it is destroyed (destructor).

"""

class Logger:
    def __init__(self):
        # Yeh constructor hai, jab object create hota hai tab yeh method automatic call hota hai
        print("Logger object created")  # Object banne par yeh message print hota hai

    def __del__(self):
        # Yeh destructor hai, jab object destroy hota hai (ya memory se hata diya jata hai) tab yeh call hota hai
        print("Logger object destroyed")  # Object destroy hone par yeh message print hota hai


# Example usage
if __name__ == "__main__":
    logger1 = Logger()  # Object create ho raha hai, constructor chalega

    # Ab object ka kaam khatam hone ke baad ya program end hone par destructor chalega
    del logger1  # Jab hum object ko delete karte hain manually, tab destructor turant call hota hai

    print("End of program")  # Yeh line destructor ke baad print ho sakti hai (depending on interpreter behavior)

""""
__init__(self) → Constructor hota hai, object bante hi call hota hai.

__del__(self) → Destructor hota hai, jab object destroy ya delete hota hai tab yeh call hota hai.

print(...) → Har method ek message print karta hai taake aapko pata chale ke object kab bana aur kab destroy hua.
"""