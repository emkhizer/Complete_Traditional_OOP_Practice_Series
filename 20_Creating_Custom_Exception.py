"""
20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. 
Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
"""
# Custom exception class banate hain
class InvalidAgeError(Exception):
    # Custom exception ko define kar rahe hain
    def __init__(self, message="Age must be 18 or older"):
        self.message = message  # Default message define kiya hai
        super().__init__(self.message)  # Parent class Exception ko call karte hain

# Function jo age ko check karega
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is below 18, which is invalid!")  # Agar age < 18 hai, toh custom exception raise karega
    else:
        print("Age is valid.")  # Agar age valid hai, toh message print karega

# Example usage
if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))  # User se age input lete hain
        check_age(age)  # Age ko check karne ke liye function call karte hain
    except InvalidAgeError as e:
        print(f"Error: {e}")  # Agar InvalidAgeError raise hota hai, toh usko handle karenge

"""
class InvalidAgeError(Exception):
➤ Yeh humari custom exception class hai jo Exception class se inherit karti hai. Humne InvalidAgeError naam diya hai is exception ko.

def __init__(self, message="Age must be 18 or older"):
➤ Yeh constructor method hai jo custom exception ke liye ek default message set karta hai. Agar exception raise hota hai, toh yeh message automatically show hoga.

super().__init__(self.message)
➤ Yeh Exception class ko call karta hai aur message ko pass karta hai jo humne define kiya hai.

def check_age(age):
➤ Yeh function hai jo age ko check karega. Agar age 18 se kam hai, toh hum InvalidAgeError exception raise karte hain.

raise InvalidAgeError("Age is below 18, which is invalid!")
➤ Agar age 18 se kam hai, toh hum custom exception InvalidAgeError ko raise karte hain aur usme custom error message pass karte hain.

try:
➤ Hum try block ke andar check_age(age) function ko call karte hain. Agar exception raise hota hai, toh except block handle karega.

except InvalidAgeError as e:
➤ Agar InvalidAgeError exception raise hota hai, toh yeh except block execute hota hai aur error message ko print karta hai.

Key Points:
Custom exceptions ka use aap apni specific errors handle karne ke liye karte hain.

Humne InvalidAgeError custom exception banaya, jo specifically age se related errors ko handle karega.

raise keyword ka use karke hum apni custom exceptions ko manually trigger karte hain.

try...except block ka use karke hum exception handling karte hain taake program crash na ho.
"""