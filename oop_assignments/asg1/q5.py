def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1, y1 = float(input("Enter x-coordinate of the first point: ")), float(input("Enter y-coordinate of the first point: "))
x2, y2 = float(input("Enter x-coordinate of the second point: ")), float(input("Enter y-coordinate of the second point: "))

distance = calculate_distance(x1, y1, x2, y2)
print("The distance between coordinate is:",calculate_distance(x1,y1,x2,y2))