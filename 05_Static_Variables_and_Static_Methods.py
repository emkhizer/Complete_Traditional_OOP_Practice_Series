""" 5. Static Variables and Static Methods Assignment:    
    Create a class MathUtils with a static method add(a, b) that returns the sum. 
    No class or instance variables should be used.
"""


class MathUtils:
    @staticmethod
    def add(a, b):
        # Yeh static method hai, isliye isme na 'self' hota hai na 'cls'
        # Yeh sirf do numbers ka sum return karega
        return a + b  # 'a' aur 'b' ka sum return kar raha hai


# Example usage
if __name__ == "__main__":
    # Static method ko call karne ke liye object banane ki zarurat nahi
    result = MathUtils.add(10, 20)  # 10 + 20 = 30, yeh result variable mein store hoga

    print(f"Sum is: {result}")  # Output: Sum is: 30

"""
@staticmethod
➤ Yeh decorator batata hai ke add method ek static method hai.
➤ Static methods na class (cls) ko use karte hain, na object (self) ko.
➤ Inka kaam simple hota hai — kisi input pe kaam karna aur result dena.

def add(a, b):
➤ Is method ko sirf do arguments milte hain: a aur b.
➤ Dono numbers ka sum kiya jaata hai.

return a + b
➤ Yeh dono numbers ka sum return karta hai.

MathUtils.add(10, 20)
➤ Static method ko class ke naam se direct call karte hain.
➤ Object banane ki bilkul zarurat nahi.
"""