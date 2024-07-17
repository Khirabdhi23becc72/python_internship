def calculate_circumference(diameter):
    radius = diameter / 2
    
    pi = 3.14159
    circumference = 2 * pi * radius
    
    return circumference

diameter = float(input("Enter the diameter of the circle: "))

circumference = calculate_circumference(diameter)

print(f"The circumference of the circle with diameter {diameter} is: {circumference}")