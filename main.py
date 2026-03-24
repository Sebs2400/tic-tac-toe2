import math  # Import section

CONSTANT_VAL = 3.14  # Global constant

def calculate_area(radius):
    """Calculates the area of a circle."""
    return CONSTANT_VAL * (radius ** 2)

def calculate(value):
    # Main execution logic
    area = calculate_area(value)
    print(f"The area is {area}")

if __name__ == "__main__":
    x = float(input('Enter user radius: '))
    calculate(x)