import math

class Circle:
    def __init__(self, x, y, radius):
        # Initialize attributes
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_area(self):
        # Calculate and return the area of the circle
        area = math.pi * self.radius**2
        return area
    
    def get_perimeter(self):
        # Calculate and return the perimeter (circumference) of the circle
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def get_circumference(self):
        # Return the circumference of the circle (same as perimeter)
        return self.get_perimeter()

# Example usage:
if __name__ == "__main__":
    circle1 = Circle(0, 0, 5)
    print(f"Area of the circle: {circle1.get_area():.2f} square units")
    print(f"Perimeter of the circle: {circle1.get_perimeter():.2f} units")
    print(f"Circumference of the circle: {circle1.get_circumference():.2f} units")
