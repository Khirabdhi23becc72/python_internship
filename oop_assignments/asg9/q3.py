# define the function
def calculate_discounted_price(original_price, discount_percent):
    discount_amount = (original_price * discount_percent) / 100
    discounted_price = original_price - discount_amount
    return discounted_price

# get user input for original price and discount percent
original_price = float(input("Enter the original price: "))
discount_percent = int(input("Enter the discount percent: "))

# use the calculate_discounted_price function
discounted_price = calculate_discounted_price(original_price, discount_percent)

# print the discounted price
print(f"Discounted price: {discounted_price:.2f}")
