def sum_of_digits(num):
    # Base case: if the number is a single digit, return the number itself
    if num < 10:
        return num
    # Recursive case: add the last digit to the sum of the digits of the remaining number
    return num % 10 + sum_of_digits(num // 10)

# Test the function
num = 12345
print(sum_of_digits(num)) 
