def solve_puzzle(total_heads, total_legs):
    # Iterate over possible number of chickens
    for num_chickens in range(total_heads + 1):
        # Calculate the number of rabbits
        num_rabbits = total_heads - num_chickens
        # Check if the current number of chickens and rabbits match the total number of legs
        if 2 * num_chickens + 4 * num_rabbits == total_legs:
            return num_chickens, num_rabbits
    return None

# Given total heads and legs
total_heads = 35
total_legs = 94

# Solve the puzzle
solution = solve_puzzle(total_heads, total_legs)

# Output the solution
if solution:
    chickens, rabbits = solution
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No solution found")
