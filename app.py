def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print(f"Add: 2 + 3 = {add(2, 3)}")
    print(f"Subtract: 5 - 2 = {subtract(5, 2)}")
    print(f"Multiply: 3 * 4 = {multiply(3, 4)}")
    print(f"Divide: 10 / 2 = {divide(10, 2)}")

# app.py

def unsafe_function():
    user_input = input("Enter something: ")
    eval(user_input)  # Danger: This allows arbitrary code execution!

if __name__ == "__main__":
    unsafe_function()
