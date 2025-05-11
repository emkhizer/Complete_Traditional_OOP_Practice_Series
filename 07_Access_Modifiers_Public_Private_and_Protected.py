"""
    7. Access Modifiers: Public, Private, and Protected Assignment:
    Create a class Employee with:

    a public variable name,

    a protected variable _salary, and

    a private variable __ssn.

    Try accessing all three variables from an object of the class and document what happens.

"""
class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable - kisi bhi jagah se directly access ho sakta hai
        self.name = name  # Public variable

        # Protected variable - convention ke mutabiq isse sirf class aur subclass mein access karna chahiye
        self._salary = salary  # Protected variable

        # Private variable - isse class ke bahar direct access nahi kiya ja sakta
        self.__ssn = ssn  # Private variable

    def display_info(self):
        # Yeh method saari info print karega
        print(f"Name: {self.name}")        # Public access
        print(f"Salary: {self._salary}")   # Protected access
        print(f"SSN: {self.__ssn}")        # Private access within class allowed


# Example usage
if __name__ == "__main__":
    emp = Employee("Ali", 50000, "123-45-6789")

    # Public variable access - yeh kaam karega
    print("Public:", emp.name)  # Output: Ali

    # Protected variable access - technically possible, lekin convention ke mutabiq avoid karna chahiye
    print("Protected:", emp._salary)  # Output: 50000

    # Private variable access - yeh directly access karne pe error dega
    try:
        print("Private:", emp.__ssn)  # ERROR: AttributeError
    except AttributeError:
        print("Private: Cannot access __ssn directly (AttributeError)")

    # Lekin agar zarurat ho to private variable ko name mangling se access kiya ja sakta hai
    print("Accessing private using name mangling:", emp._Employee__ssn)  # Output: 123-45-6789

    # Display method ke zariye saari info access ho sakti hai
    emp.display_info()

"""
self.name
➤ Public variable hai. Isse kahin se bhi directly access kar sakte hain, koi restriction nahi hoti.

self._salary
➤ Protected variable hai. Yeh ek convention hai — yeh suggest karta hai ke isse class ke bahar direct 
use na karein, lekin technically allowed hai.

self.__ssn
➤ Private variable hai. Yeh class ke bahar direct access nahi hota. Python isse internally name mangling 
ke zariye _ClassName__variableName bana deta hai.

emp.__ssn
➤ Yeh access attempt fail hoga — AttributeError aayega.

emp._Employee__ssn
➤ Yeh name mangling ka use karke private variable ko access karta hai. Allowed hai, lekin secure nahi maana jata.
"""