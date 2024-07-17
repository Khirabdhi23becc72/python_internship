def is_perfect_square(n):
    return int(n**0.5)**2 == n

user_input = int(input("Enter a number: "))
if is_perfect_square(user_input):
    print(f"{user_input} is a perfect square.")
else:
    print(f"{user_input} is not a perfect square.")
