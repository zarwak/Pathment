"""
calculator.py - A simple calculator to practice Git version control.
This file will be used to simulate branching, merging, and conflict resolution.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Demonstrate the calculator functions."""
    print("=== Simple Calculator ===")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

if __name__ == "__main__":
    main()