class Product:
    def _init_(self, product_id, name, price, discount_percentage):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__discount_percentage = discount_percentage

    # Getter and Setter for product_id
    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getter and Setter for price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    # Getter and Setter for discount_percentage
    @property
    def discount_percentage(self):
        return self.__discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        self.__discount_percentage = discount_percentage

    # Protected method to calculate the final price after discount
    def _final_price(self):
        return self._price * (1 - self._discount_percentage / 100)

class Electronics(Product):
    def _init_(self, product_id, name, price, discount_percentage, warranty_period):
        super()._init_(product_id, name, price, discount_percentage)
        self.__warranty_period = warranty_period

    # Getter and Setter for warranty_period
    @property
    def warranty_period(self):
        return self.__warranty_period

    @warranty_period.setter
    def warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period

class Clothing(Product):
    def _init_(self, product_id, name, price, discount_percentage, size, material):
        super()._init_(product_id, name, price, discount_percentage)
        self.__size = size
        self.__material = material

    # Getter and Setter for size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    # Getter and Setter for material
    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material

class ShoppingCart:
    def _init_(self):
        self.products = []

    def add_electronic_item(self, electronic_item):
        self.products.append(electronic_item)

    def add_clothing_item(self, clothing_item):
        self.products.append(clothing_item)

    def display_all_products(self):
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Final Price: {product._final_price():.2f}")

    def calculate_total_price(self, tax_rate=0.10):
        total = sum(product._final_price() for product in self.products)
        total_with_tax = total * (1 + tax_rate)
        print(f"Total price including tax: {total_with_tax:.2f}")

# Example usage
shopping_cart = ShoppingCart()

# Adding electronic items
electronic1 = Electronics("E1001", "Laptop", 1000, 10, "2 years")
electronic2 = Electronics("E1002", "Smartphone", 800, 5, "1 year")
electronic3 =  Electronics("E1003","remote",500,3,"1 year")
shopping_cart.add_electronic_item(electronic1)
shopping_cart.add_electronic_item(electronic2)
shopping_cart.add_electronic_item(electronic3)

# Adding clothing items
clothing1 = Clothing("C1001", "T-shirt", 20, 15, "M", "Cotton")
clothing2 = Clothing("C1002", "Jeans", 50, 10, "L", "Denim")
shopping_cart.add_clothing_item(clothing1)
shopping_cart.add_clothing_item(clothing2)

# Display all products
print("Products:")
shopping_cart.display_all_products()

# Calculate and display the total price including tax
print("\nTotal Price:")
shopping_cart.calculate_total_price()