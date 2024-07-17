# Take two list of numbers the products quantities and the prices. Calculate total price per product.
product_quantities = [13, 5, 6, 10, 11]
prices = [1.2, 6.5, 1.0, 4.8, 5.0]

# Calculate using list comprehension
total_price_per_product = [product_quantities[i] * prices[i] for i in range(len(product_quantities))]

# Sum up the total prices to get the final output
total_price = sum(total_price_per_product)

# Print the total price
print(total_price)
