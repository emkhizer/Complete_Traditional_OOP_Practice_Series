"""
11. Class Methods Assignment:
Create a class Book with a class variable total_books. 
Add a class method increment_book_count() to increase the count when a new book is added.
"""
class Book:
    # Class variable - yeh sab objects ke liye common hota hai
    total_books = 0  # Shuru mein total_books 0 hai

    def __init__(self, title):
        # Jab bhi naya book object banega, uska title set hoga
        self.title = title  # Instance variable

        # Har baar naya book banne par count increase karna hai
        Book.increment_book_count()  # Class method ko call kar rahe hain

    @classmethod
    def increment_book_count(cls):
        # Class method - 'cls' class ko refer karta hai
        # total_books ko 1 se increase karega
        cls.total_books += 1  # Class variable update ho raha hai

    @classmethod
    def display_total_books(cls):
        # Total books ka current count dikhata hai
        print(f"Total books: {cls.total_books}")


# Example usage
if __name__ == "__main__":
    book1 = Book("Python Basics")       # 1st book banaya
    book2 = Book("Advanced Python")     # 2nd book banaya
    book3 = Book("Data Structures")     # 3rd book banaya

    # Ab total_books ka count check karte hain
    Book.display_total_books()  # Output: Total books: 3
"""
total_books = 0
➤ Ye class variable hai, har new book object banne par yeh variable sab ke liye update hota hai.

def __init__(self, title):
➤ Jab naya object banta hai, tab title set hota hai aur class method increment_book_count() call hoti hai.

@classmethod
➤ Is decorator se method class ke level par kaam karta hai, isliye cls use hota hai instead of self.

cls.total_books += 1
➤ Har baar jab new object banta hai, total_books ko 1 se bada dete hain.

display_total_books()
➤ Ye class method current total book count print karta hai.
"""