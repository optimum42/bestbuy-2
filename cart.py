class Cart:
    """
    The Cart class that holds all products in the shopping cart
    and manages the addition, removal, and total price of the products
    """

    def __init__(self, new_products=None):
        new_products = new_products or {}
        self.products = new_products

    def is_empty(self):
        return not self.products

    def add_product(self, product, quantity=1):
        if not product.is_active():
            raise ValueError(f"{product.name}: Product not available")

        total_quantity = quantity
        if product in self.products:
            total_quantity += self.products[product]

        if total_quantity < 0:
            raise ValueError(
                f"{product.name}: Total cart quantity cannot be negative")

        if total_quantity == 0:
            if product in self.products:
                del self.products[product]

        if total_quantity > 0:
            product.check_quantity(total_quantity)
            self.products[product] = total_quantity

    def show(self):
        if not self.products:
            print("*** Your cart is empty!")
            return

        print("\n*** Your cart:")
        for product, quantity in self.products.items():
            # Prüfen, ob eine Promo existiert, um den reduzierten Preis und einen Text anzuzeigen
            if product.promotion:
                line_price = product.promotion.apply_promotion(product,
                                                               quantity)
                promo_text = f" [Promo: {product.promotion.name}]"
            else:
                line_price = product.get_price() * quantity
                promo_text = ""

            print(
                f"{quantity:,.0f} {product.name} (${product.price:,.2f}){promo_text} = ${line_price:,.2f}")

    def get_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            # Die Gesamtsumme muss die Promotions berücksichtigen
            if product.promotion:
                total_price += product.promotion.apply_promotion(product,
                                                                 quantity)
            else:
                total_price += product.get_price() * quantity

        return total_price