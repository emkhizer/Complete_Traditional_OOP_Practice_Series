"""
15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
"""
class A:
    def show(self):
        # A ka show method jo base class mein hai
        print("Method from Class A")

class B(A):
    def show(self):
        # B mein show method ko override kiya gaya hai
        print("Method from Class B")

class C(A):
    def show(self):
        # C mein show method ko override kiya gaya hai
        print("Method from Class C")

class D(B, C):
    # D class, B aur C dono se inherit kar rahi hai
    pass

# Example usage
if __name__ == "__main__":
    d = D()  # D ka object bana rahe hain
    d.show()  # show() method call karte hain

"""
class A:
➤ Yeh class A define karti hai jisme ek method show() hai jo print karega "Method from Class A".

class B(A):
➤ Yeh class B hai jo A class se inherit kar rahi hai. B ke andar show() method ko override kiya gaya 
hai aur "Method from Class B" print hoga.

class C(A):
➤ Yeh class C bhi A class se inherit kar rahi hai aur isme bhi show() method ko override kiya gaya hai. 
Isme print hoga "Method from Class C".

class D(B, C):
➤ Yeh class D hai jo B aur C dono se inherit kar rahi hai. 
Is case mein, D class ko pehle B se aur phir C se methods milenge.

Method Resolution Order (MRO):
Jab hum d.show() call karte hain, Python MRO ko follow karke method resolve karta hai.

Python ka MRO ye decide karta hai ke kis class ka method call hoga. Yahan D class B aur C se inherit kar rahi hai, 
aur B A se inherit karta hai, isliye MRO yeh hota hai:

D → B → C → A

Jab hum d.show() call karte hain, Python sabse pehle B ka method dekhne ki koshish karta hai, 
kyunki B C se pehle aata hai MRO ke according. 
Isliye B ka show() method call hota hai aur "Method from Class B" print hota hai.

Key Points:

Diamond Inheritance hota hai jab ek class do ya zyada classes se inherit karti hai, 
jo apne aap base class se inherit kar rahi hoti hain.

MRO (Method Resolution Order) Python ka mechanism hai jo define karta hai ke kis order 
mein methods ko call kiya jayega jab ek class multiple inheritance ka use kar rahi ho.

Python C3 Linearization Algorithm ko follow karta hai jab MRO decide karta hai.
"""