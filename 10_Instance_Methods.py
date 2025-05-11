"""
10. Instance Methods Assignment:
Create a class Dog with instance variables name and breed. 
Add an instance method bark() that prints a message including the dog's name.
"""
class Dog:
    def __init__(self, name, breed):
        # Constructor jab object banega tab run hota hai
        # Instance variables set ho rahe hain: name aur breed
        self.name = name      # Dog ka naam
        self.breed = breed    # Dog ki breed

    def bark(self):
        # Instance method bark — ye 'self' ka use karta hai object ki info access karne ke liye
        print(f"{self.name} is barking!")  # Dog ke naam ke sath barking message print karega


# Example usage
if __name__ == "__main__":
    dog1 = Dog("Tommy", "Labrador")  # Dog ka object create kar rahe hain

    dog1.bark()  # bark method call kar rahe hain — output: Tommy is barking!

"""
self.name aur self.breed
➤ Ye instance variables hain — har object ka apna alag naam aur breed hoga.

def bark(self):
➤ Ye ek instance method hai — isme self likhna zaroori hota hai taake object ki values (name, breed) ko use kiya ja sake.

dog1 = Dog("Tommy", "Labrador")
➤ Ye ek object bana raha hai jiska naam Tommy hai aur breed Labrador.

dog1.bark()
➤ Ye method call karega aur message print karega: "Tommy is barking!"


"""