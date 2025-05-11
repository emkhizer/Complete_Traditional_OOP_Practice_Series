"""
8. The super() Function Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, 
add a subject field, and use super() to call the base class constructor.
"""
class Person:
    def __init__(self, name):
        # Constructor of base class (Person)
        # Jab object banega, yeh name set karega
        self.name = name  # Public variable name


class Teacher(Person):  # Teacher class Person se inherit kar rahi hai
    def __init__(self, name, subject):
        # super() ka use karke parent class (Person) ka constructor call karte hain
        super().__init__(name)  # Yeh line Person ka __init__ call karti hai taake name set ho jaye

        # Teacher class ka apna variable
        self.subject = subject  # Teacher ka subject set karte hain


    def display_info(self):
        # Yeh method name aur subject dono print karega
        print(f"Name: {self.name}")        # Inherited variable
        print(f"Subject: {self.subject}")  # Teacher ka apna variable
        

# Example usage
if __name__ == "__main__":
    t1 = Teacher("Miss Sana", "Mathematics")  # Teacher object bana rahe hain

    t1.display_info()  # Info print hogi: name aur subject dono
"""
class Person:
➤ Yeh base (parent) class hai, jo name handle karti hai.

class Teacher(Person):
➤ Yeh child class hai jo Person se inherit karti hai.

super().__init__(name)
➤ Yeh Person class ka constructor call karta hai taake name ka kaam Person handle kare.

self.subject = subject
➤ Teacher class ka apna additional data — subject — yahan set hota hai.

display_info()
➤ Yeh method inherited (name) aur apna (subject) dono values show karta hai.

"""