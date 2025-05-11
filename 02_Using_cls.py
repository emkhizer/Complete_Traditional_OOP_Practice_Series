""" 2. Using cls Assignment:
    Create a class Counter that keeps track of how many objects have been created. 
    Use a class variable and a class method with cls to manage and display the count.
"""
class Counter:
    # Yeh class variable hai jo object count ko track karega
    count = 0  # Initially count ko 0 set kar rahe hain

    def __init__(self):
        # Yeh constructor method hai jo har baar naya object banne par call hota hai
        # Jab bhi naya object create hoga, count ko 1 se increase karenge
        Counter.count += 1  # Counter.count ka matlab hai class ka count variable, jo sab objects ke liye common hai

    @classmethod
    def display_count(cls):
        # Yeh class method hai jo count ko display karega
        # 'cls' ka matlab hai class, aur isme hum class ka variable 'count' access karte hain
        print(f"Number of objects created: {cls.count}")  # Yeh current count ko print karne ke liye hai


# Example usage
if __name__ == "__main__":
    # Counter ke objects banane ke liye
    counter1 = Counter()  # Pehla object create ho gaya, count 1 ho jayega
    counter2 = Counter()  # Doosra object create ho gaya, count 2 ho jayega
    counter3 = Counter()  # Teesra object create ho gaya, count 3 ho jayega

    # Total objects ka count display karne ke liye
    Counter.display_count()  # Yahan pe display_count method ko class ke naam se call kiya gaya hai
    # Output: Number of objects created: 3
