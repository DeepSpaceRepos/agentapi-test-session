def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main function to demonstrate the calculator functions."""
    print("Python Calculator")
    print("================")
    
    # Test the calculator functions
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    print(f"Division: 10 / 5 = {divide(10, 5)}")
    
    # Test division by zero
    try:
        print(f"Division by zero: 10 / 0 = {divide(10, 0)}")
    except ValueError as e:
        print(f"Division by zero: {e}")

if __name__ == "__main__":
    main()