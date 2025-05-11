"""
19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() 
method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
"""
class Multiplier:
    def __init__(self, factor):
        # Factor ko initialize karte hain jo multiplication mein use hoga
        self.factor = factor

    # __call__ method define kar rahe hain jo object ko function ki tarah behave karne dega
    def __call__(self, value):
        return value * self.factor  # Input ko factor se multiply karenge

# Example usage
if __name__ == "__main__":
    multiply_by_2 = Multiplier(2)  # Multiplier ka object banate hain jisme factor 2 hai

    # callable() function se check kar rahe hain agar multiply_by_2 callable hai
    print(callable(multiply_by_2))  # Output: True, kyunki object __call__ method define karta hai

    # Object ko function ki tarah call kar rahe hain
    result = multiply_by_2(5)  # 5 ko multiply_by_2 ke factor se multiply karenge (5 * 2)
    print(result)  # Output: 10

"""
class Multiplier:
➤ Yeh class Multiplier ko define kar rahi hai, jisme ek factor hoga jo multiplication ke liye use hoga.

def __init__(self, factor):
➤ Yeh constructor method hai jo class ko initialize karte waqt factor set karega. 
Yeh wo value hogi jo hum input ko multiply karne ke liye use karenge.

def __call__(self, value):
➤ Yeh special method __call__() hai jo kisi object ko function ki tarah call karne ka functionality deta hai. 
Jab hum object ko function ki tarah call karenge, yeh method execute hoga. 
Is method mein, hum input value ko self.factor se multiply karte hain.

print(callable(multiply_by_2))
➤ callable() function check karta hai ke kya multiply_by_2 object ko function ki tarah call kiya ja sakta hai. 
Agar __call__() method defined hai, toh yeh return karega True.

result = multiply_by_2(5)
➤ Hum multiply_by_2 object ko 5 ke saath function ki tarah call kar rahe hain. Yeh __call__() 
method ko invoke karega aur 5 * 2 ka result return karega.

Key Points:
__call__() method ek special method hai jo kisi object ko function ki tarah call karne ka capability deta hai.

Jab hum multiply_by_2(5) likhte hain, yeh __call__() method ko execute karta hai, jo 5 ko 2 (factor) se multiply kar deta hai.

callable() function check karta hai ki koi object callable hai ya nahi. Agar object ke andar __call__() method defined hai, 
toh wo object callable hoga aur callable() True return karega.

"""