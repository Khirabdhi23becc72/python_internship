def is_valid_triangle(a, b, c):
    # Check if the given sides form a valid triangle using the triangle inequality theorem
    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c):
    # Classify the triangle based on its sides
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Right-angled"
    else:
        return "Scalene"

def circumcenter_radius(a, b, c):
    # Check if the sides form a valid triangle
    if not is_valid_triangle(a, b, c):
        return -1
    
    # Calculate the radius of the circumcenter if the triangle is right-angled
    if classify_triangle(a, b, c) == "Right-angled":
        # For a right-angled triangle, the circumradius is half the hypotenuse
        hypotenuse = max(a, b, c)
        return hypotenuse / 2
    else:
        return -1

# Example usage
a = 3
b = 4
c = 5

if is_valid_triangle(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print(f"The triangle is {triangle_type}.")
    radius = circumcenter_radius(a, b, c)
    print(f"The radius of the circumcenter is {radius}.")
else:
    print("The given sides do not form a valid triangle.")
