"""
14. Aggregation
Assignment:
Create a class Department and a class Employee. 
Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

"""
# Employee class define kar rahe hain
class Employee:
    def __init__(self, name, role):
        # Employee ka constructor jo name aur role set karega
        self.name = name  # Employee ka naam
        self.role = role  # Employee ka role

    def display_info(self):
        # Employee ka info print karne wala method
        print(f"Name: {self.name}, Role: {self.role}")

# Department class define kar rahe hain
class Department:
    def __init__(self, dept_name, employee):
        # Department ka constructor jisme employee ka object pass hota hai
        self.dept_name = dept_name  # Department ka naam
        self.employee = employee    # Department ke paas ek employee ka reference hoga

    def display_department_info(self):
        # Department ki info aur employee ka info show karega
        print(f"Department: {self.dept_name}")
        self.employee.display_info()  # Employee ka info display karne ke liye method call kar rahe hain


# Example usage
if __name__ == "__main__":
    # Pehle ek employee ka object banate hain
    emp1 = Employee("Ali", "Software Engineer")

    # Department ka object bana rahe hain, aur usme employee ka reference pass kar rahe hain
    dept1 = Department("IT", emp1)

    # Department ke info ko display karte hain
    dept1.display_department_info()

"""
class Employee:
➤ Yeh class Employee ko define karti hai jisme name aur role attributes hain.

class Department:
➤ Yeh class Department ko define karti hai, jisme ek Employee ka object reference store kiya gaya hai. 
Yeh aggregation ka example hai, kyunki Employee ka object Department ke andar hai, lekin independently exist karta hai.

self.employee = employee
➤ Yahan Department ka object Employee ka reference store kar raha hai. 
Yeh aggregation ka concept hai — Department ko employee ki zarurat hai, 
lekin employee ka object independently exist kar raha hai aur kisi aur jagah use ho sakta hai.

self.employee.display_info()
➤ Department class ka method Employee ke method ko call karta hai aur uski details print karta hai.


Aggregation ka matlab hai: "has-a" relationship jahan ek object doosre object ka reference rakhta hai, 
lekin dono objects apne aap independent rehte hain.

Is example mein, Department ko employee ka reference diya gaya hai, lekin Employee ka object Department se 
independently exist karta hai. Agar aap employee ka object delete karenge toh department unaffected rahega, 
isliye dono objects independent hain.

Agar aap kisi object ko department ke baad bhi use karna chahein, toh wo possible hai, kyunki dono ka relationship 
aggregation ke through hai.
"""