
class Product:
    """
    The product class that holds the product name, price, and quantity
    and allows the user to operate on the product
    """
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError(f"{name}: Name cannot be empty")
        self.name = name

        if price <= 0:
            raise ValueError(f"{name}: Price must be greater than 0")
        self.price = price

        if quantity <= 0:
            raise ValueError(f"{name}: Quantity must be greater than 0")
        self.quantity = quantity

        self.active = True

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError(f"{self.name}: Quantity must be greater than 0")
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price:,.2f}, Quantity: {self.quantity:,.0f}")

    def check_quantity(self, quantity):
        """ Verifies if the quantity as allowed to be bought """
        if quantity <= 0:
            raise ValueError(f"{self.name}: Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError(
                f"{self.name}: {quantity:,.0f} exceeds the maximum quantity of {self.quantity:,.0f}")

    def buy(self, quantity):
        self.check_quantity(quantity)

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return quantity * self.price


class NonStockedProduct(Product):
    """
    Non-physical products like software licenses.
    Quantity is always 0 and does not decrease upon purchase.
    """

    def __init__(self, name, price):
        # We pass a dummy quantity (1) to super() to bypass the parent's
        # quantity <= 0 validation, and then immediately set it to 0.
        super().__init__(name, price, 1)
        self.quantity = 0

    def check_quantity(self, quantity):
        # Digitale Produkte haben unendlich viel "Bestand".
        # Wir prüfen hier also nur noch, ob die Eingabe überhaupt Sinn macht (> 0).
        if quantity <= 0:
            raise ValueError(f"{self.name}: Quantity must be greater than 0")

    def buy(self, quantity):
        self.check_quantity(quantity)

        # skip the quantity subtraction and active status checks
        # because this product has infinite digital stock.
        return quantity * self.price

    def show(self):
        # Overriding to show it's a non-stocked item
        print(
            f"{self.name}, Price: ${self.price:,.2f}, Quantity: Unlimited (Non-Stocked)")


class LimitedProduct(Product):
    """
    Products that have a maximum purchase limit per order.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def check_quantity(self, quantity):
        # Check for limited products
        if quantity > self.maximum:
            raise ValueError(
                f"{self.name}: Cannot buy more than {self.maximum} in a single order")

        # Base class check
        super().check_quantity(quantity)

    def buy(self, quantity):
        self.check_quantity(quantity)

        # The parent class handles the standard validation and quantity adjusting
        return super().buy(quantity)

    def show(self):
        # Overriding to display the maximum limit
        print(
            f"{self.name}, Price: ${self.price:,.2f}, "
            f"Quantity: {self.quantity:,.0f}, Max per order: {self.maximum}")


def main():
    try:
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        print(bose.buy(50))
        print(mac.buy(100))
        print(mac.is_active())

        bose.show()
        mac.show()

        bose.set_quantity(1000)
        bose.show()

        product_list = [
                Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250,
                                 quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
                NonStockedProduct("Windows License", price=125),
                LimitedProduct("Shipping", price=10, quantity=250,
                                    maximum=1)
            ]
        for product in product_list:
            product.show()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

