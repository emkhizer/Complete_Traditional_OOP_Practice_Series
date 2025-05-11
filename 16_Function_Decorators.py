""" 16. Function Decorators
    Assignment:
    Write a decorator function log_function_call that prints "Function is being called" before a function executes. 
    Apply it to a function say_hello().
"""
# Decorator function jo function call hone se pehle message print karega
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Message jo function call hone se pehle print hoga
        func()  # Original function ko call karenge
    return wrapper  # Wrapper function ko return kar rahe hain

# say_hello function ko decorator ke saath apply karte hain
@log_function_call
def say_hello():
    print("Hello, world!")  # Yeh actual function ka kaam hai

# Example usage
if __name__ == "__main__":
    say_hello()  # say_hello function ko call karenge
"""
def log_function_call(func):
➤ Yeh ek decorator function hai jo kisi bhi function ko wrap karega. 
Isme func parameter uss function ko represent karta hai jo decorator ke through pass kiya gaya hai.

def wrapper():
➤ Yeh ek wrapper function hai jo original function ke aage apni functionality add karega (yahan hum message print karenge).

print("Function is being called")
➤ Yeh message print hoga jab bhi wrapped function call hoga. 
Matlab, before function executes yeh message show hoga.

func()
➤ Yeh original function ko call karega jo decorator ke andar pass kiya gaya hai, is case mein say_hello().

@log_function_call
➤ Yeh syntax decorator ko function ke upar apply karne ke liye hota hai. 
Jab hum @log_function_call likhte hain, 
toh say_hello() function ko log_function_call decorator ke through wrap kiya jata hai.

say_hello()
➤ Jab hum say_hello() call karte hain, yeh sabse pehle log_function_call decorator ko call karega, 
jisme message "Function is being called" print hoga. 
Uske baad original function, say_hello, execute hoga aur "Hello, world!" print hoga.
"""