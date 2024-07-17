# Given a list of products, print out the name of all the products with a price higher than 10
products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]

# Using dictionary to get the product names with price higher than 10
expensive_products = {product['name']: product['price'] for product in products if product['price'] > 10}

# Print the names of the expensive products
print(expensive_products.keys())
