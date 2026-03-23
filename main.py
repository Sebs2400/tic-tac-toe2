import math  # Import section

CONSTANT_VAL = 3.14  # Global constant

def calculate_area(radius):
    """Calculates the area of a circle."""
    return math.pi * (radius ** 2)

def main():
    # Main execution logic
    user_radius = 5
    area = calculate_area(user_radius)
    print(f"The area is {area}")

if __name__ == "__main__":
    main()