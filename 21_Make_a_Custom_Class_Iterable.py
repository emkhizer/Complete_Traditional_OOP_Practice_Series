"""
21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. 
Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
"""
class Countdown:
    def __init__(self, start):
        self.start = start  # Initial start number ko store karte hain
        self.current = start  # Current number bhi start se initialize karte hain

    # __iter__ method ko define kar rahe hain jo iterable banaata hai
    def __iter__(self):
        return self  # Hum apne object ko return karte hain taake for-loop ke liye iterable ho

    # __next__ method ko define kar rahe hain jo iteration ko handle karega
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Agar countdown 0 tak pohnch gaya ho, toh iteration ko stop karenge
        else:
            self.current -= 1  # Countdown ko ek number reduce karte hain
            return self.current  # Current number return karte hain

# Example usage
if __name__ == "__main__":
    countdown = Countdown(5)  # Countdown ko 5 se start kar rahe hain

    for num in countdown:  # Countdown object ko for-loop mein use karenge
        print(num)  # Har iteration par countdown number print hoga
