"""
    18. Property Decorators: @property, @setter, and @deleter Assignment:
    Create a class Product with a private attribute _price. 
    Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
"""

class Product:
    def __init__(self, price):
        # Private attribute _price
        self._price = price

    # @property decorator ke zariye price ko read karne ka method
    @property
    def price(self):
        return self._price  # Price ko return karenge

    # @price.setter decorator ke zariye price ko update karne ka method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")  # Agar price negative ho toh error print karenge
        else:
            self._price = value  # Price ko update karenge

    # @price.deleter decorator ke zariye price ko delete karne ka method
    @price.deleter
    def price(self):
        print("Deleting price...")  # Jab price delete ho, message print hoga
        del self._price  # Price ko delete karenge


# Example usage
if __name__ == "__main__":
    product = Product(100)  # Product ka object bana rahe hain, initial price 100 hai
    
    print("Initial Price:", product.price)  # price ko access kar rahe hain, yeh getter ko call karega

    product.price = 150  # price ko update kar rahe hain, yeh setter ko call karega
    print("Updated Price:", product.price)

    product.price = -50  # Negative price set karne ki koshish, setter message show karega

    del product.price  # price ko delete kar rahe hain, yeh deleter ko call karega
"""
class Product:
➤ Yeh class Product ko define karti hai. Isme private attribute _price hoga jo initial price ko store karega.

@property
➤ Yeh decorator price ko getter banata hai. Jab hum product.price access karte hain, 
toh yeh @property method ko call karega aur price return karega.

@price.setter
➤ Yeh decorator price ko setter bana deta hai. Jab hum product.price = 150 likhte hain, 
yeh setter method ko call karega aur price ko update karega. Agar price negative set karne 
ki koshish ki jati hai, toh ek message print hoga "Price cannot be negative!".

@price.deleter
➤ Yeh decorator price ko deleter bana deta hai. Jab hum del product.price karte hain, 
yeh deleter method ko call karta hai aur _price ko delete karne se pehle "Deleting price..." message print hota hai.

Key Points:
@property ka use karke hum kisi private attribute ko publically access kar sakte hain bina direct attribute ko expose kiye.

@setter ka use karke hum kisi attribute ko update karne ka logic add kar sakte hain.

@deleter ka use karke hum kisi attribute ko delete karne ka functionality add kar sakte hain.

Yeh decorators ek simple aur effective tarika hai apne code ko clean aur safe rakhne ke liye 
jab aapko kisi private attribute ko control karna ho.
"""