def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    print("Welcome to the Arithmetic Operations Program")
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 and 3:", subtract(5, 3))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 5 by 3:", divide(5, 3))

