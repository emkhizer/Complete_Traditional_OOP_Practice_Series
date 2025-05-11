"""
12. Static Methods Assignment:
Create a class Temperature Converter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Static method hai, isme na 'self' use hota hai na 'cls'
        # Sirf input le kar result return karta hai
        return (c * 9/5) + 32  # Celsius se Fahrenheit convert karne ka formula


# Example usage
if __name__ == "__main__":
    temp_c = 25  # 25 degree Celsius

    temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)  # Static method ko class name se call kiya

    print(f"{temp_c}°C is equal to {temp_f}°F")  # Output print hoga

"""
@staticmethod
➤ Isse method ban jata hai static — yaani yeh kisi object ya class variable pe depend nahi karta.

def celsius_to_fahrenheit(c):
➤ Yeh method ek argument c (Celsius) leta hai aur Fahrenheit mein convert karke return karta hai.

return (c * 9/5) + 32
➤ Celsius to Fahrenheit ka standard formula use kiya gaya hai.

TemperatureConverter.celsius_to_fahrenheit(temp_c)
➤ Static method ko direct class ke naam se call kiya — object banane ki zarurat nahi.
"""