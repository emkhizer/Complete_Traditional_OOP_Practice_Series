""" 1. Using self Assignment:
    Create a class Student with attributes name and marks. 
    Use the self keyword to initialize these values via a constructor. 
    Add a method display() that prints student details.
"""
class Student:
    def __init__(self, name, marks):
        # Yeh __init__ method hai, jo constructor ka kaam karta hai
        # Jab hum naya student ka object banate hain, yeh method automatically call hota hai
        self.name = name  # 'self.name' mein student ka naam store hota hai
        self.marks = marks  # 'self.marks' mein student ke marks store hote hain

    def display(self):
        # Yeh display() method student ke details print karne ke liye hai
        print(f"Student Name: {self.name}")  # 'self.name' se student ka naam print karte hain
        print(f"Student Marks: {self.marks}")  # 'self.marks' se student ke marks print karte hain


# Example usage
if __name__ == "__main__":
    # Student ka object banane ke liye, hum Student class ka use karte hain
    # Hum yahan pe "Alice" naam aur 85 marks ke saath student1 ka object bana rahe hain
    student1 = Student("Alice", 85)

    # student1 ke details display karne ke liye display() method call karte hain
    student1.display()
