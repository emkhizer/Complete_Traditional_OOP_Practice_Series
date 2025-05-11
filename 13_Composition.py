"""
    13. Composition
    Assignment:
    Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. 
    Access a method of the Engine class via the Car class.
"""

# Engine class define kar rahe hain
class Engine:
    def start(self):
        # Engine ka method jo start hone par message deta hai
        print("Engine started")  # Jab engine start hoga, yeh print hoga


# Car class define kar rahe hain
class Car:
    def __init__(self, engine):
        # Composition: Car class ke andar Engine object pass kar rahe hain
        self.engine = engine  # Car ke paas ek engine object hoga

    def start_car(self):
        # Car ka method engine ka start() method call karega
        print("Starting the car...")
        self.engine.start()  # Engine ka method call ho raha hai composition ke through


# Example usage
if __name__ == "__main__":
    my_engine = Engine()          # Pehle Engine object banaya
    my_car = Car(my_engine)       # Engine object Car mein pass kiya (composition)

    my_car.start_car()            # Car ka method call kar rahe hain jo engine ko start karega

"""
class Engine:
➤ Yeh ek simple class hai jisme ek method start() hai.

class Car:
➤ Yeh doosri class hai jo Engine ka object receive karti hai constructor me. Yeh composition ka example hai.

self.engine = engine
➤ Car ke andar engine ka object store kiya ja raha hai — ab Car ke paas ek Engine bhi hai.

self.engine.start()
➤ Car ke method ke through hum Engine ka method access kar rahe hain — composition ka real use.

"""