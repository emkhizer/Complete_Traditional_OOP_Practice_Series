""" 4. Class Variables and Class Methods Assignment:
    Create a class Bank with a class variable bank_name. 
    Add a class method change_bank_name(cls, name) that allows changing the bank name. 
    Show that it affects all instances.
"""

class Bank:
    # Yeh ek class variable hai jo bank ka naam store karega
    bank_name = "ABC Bank"  # Default bank name set kiya gaya hai

    @classmethod
    def change_bank_name(cls, name):
        # Yeh ek class method hai jo bank ka naam change karega
        # 'cls' se hum class variable ko access kar rahe hain aur uska naam change kar rahe hain
        cls.bank_name = name  # Hum class variable 'bank_name' ko new naam se update karte hain

    def display_bank_name(self):
        # Yeh instance method hai jo current bank name ko display karega
        # Hum 'self.bank_name' se class variable ko access karte hain, jo sab instances ke liye common hai
        print(f"Bank Name: {self.bank_name}")  # Yahan pe bank ka naam print ho raha hai


# Example usage
if __name__ == "__main__":
    # Bank class ka pehla object create kar rahe hain
    bank1 = Bank()  # Pehla bank object

    # Bank class ka doosra object create kar rahe hain
    bank2 = Bank()  # Doosra bank object

    # Initial bank name dono objects ke liye display kar rahe hain
    bank1.display_bank_name()  # Bank1 ka naam display hoga: "ABC Bank"
    bank2.display_bank_name()  # Bank2 ka naam display hoga: "ABC Bank"

    # Bank ka naam change kar rahe hain class method ke zariye
    Bank.change_bank_name("XYZ Bank")  # Ab sab objects ka bank name "XYZ Bank" ho jayega

    # Naya bank name display kar rahe hain dono objects ke liye
    bank1.display_bank_name()  # Ab bank1 ka naam "XYZ Bank" ho gaya hai
    bank2.display_bank_name()  # Ab bank2 ka naam bhi "XYZ Bank" ho gaya hai
