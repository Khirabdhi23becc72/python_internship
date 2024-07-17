from abc import ABC, abstractmethod

# Abstract class PaymentMethod
class PaymentMethod(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def pay(self, amount):
        pass

# Subclass CreditCard
class CreditCard(PaymentMethod):
    def __init__(self, cc_no, exp_date, cvv):
        super().__init__()
        self.cc_no = cc_no
        self.exp_date = exp_date
        self.cvv = cvv
    
    def pay(self, amount):
        # Simulate credit card payment process
        print(f"Paying ${amount} using Credit Card ending with {self.cc_no[-4:]}")

# Subclass PayPal
class PayPal(PaymentMethod):
    def __init__(self, email):
        super().__init__()
        self.email = email
    
    def pay(self, amount):
        # Simulate PayPal payment process
        print(f"Paying ${amount} using PayPal account {self.email}")

# Subclass Bitcoin
class Bitcoin(PaymentMethod):
    def __init__(self, wallet_add):
        super().__init__()
        self.wallet_add = wallet_add
    
    def pay(self, amount):
        # Simulate Bitcoin payment process
        print(f"Paying ${amount} using Bitcoin wallet address {self.wallet_add}")

# Example usage:
if __name__ == "__main__":
    # Creating instances of each subclass
    credit_card = CreditCard(cc_no="1234567812345678", exp_date="12/23", cvv="123")
    paypal = PayPal(email="example@example.com")
    bitcoin = Bitcoin(wallet_add="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # Making payments
    amount = 100.0
    credit_card.pay(amount)
    paypal.pay(amount)
    bitcoin.pay(amount)
