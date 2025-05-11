""" 3. Public Variables and Methods Assignment:
    Create a class Car with a public variable brand and a public method start().
    Instantiate the class and access both from outside the class.
"""


class Car:
    # Public variable 'brand'
    brand = "Toyota"  # Car ka brand, yeh public hai aur hum isse directly access kar sakte hain

    # Public method 'start'
    def start(self):
        print(
            f"The {self.brand} car is now starting..."
        )  # Car start hone ka message display karta hai


# Example usage
if __name__ == "__main__":
    # Car class ka object banate hain
    my_car = Car()

    # Public variable 'brand' ko directly access karte hain
    print(f"My car's brand is: {my_car.brand}")  # Output: My car's brand is: Toyota

    # Public method 'start' ko call karte hain
    my_car.start()  # Output: The Toyota car is now starting...
