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
        # 1. Ist das Produkt überhaupt aktiv?
        if not product.is_active():
            raise ValueError(f"{product.name}: Product not available")

        # 2. Berechne die zukünftige Gesamtmenge dieses Produkts im Warenkorb
        total_quantity = quantity
        if product in self.products:
            total_quantity += self.products[product]

        # 3. Logische Warenkorb-Prüfungen
        if total_quantity < 0:
            raise ValueError(
                f"{product.name}: Total cart quantity cannot be negative")

        if total_quantity == 0:
            if product in self.products:
                del self.products[product]

        # 4. Die Magie des Polymorphismus: Das Produkt validiert die Menge selbst!
        if total_quantity > 0:
            # Wir rufen die check_quantity Methode auf, die wir in Product.py definiert haben.
            # Egal ob normales, digitales oder limitiertes Produkt: Es weiß selbst, was erlaubt ist!
            product.check_quantity(total_quantity)

            # Wenn check_quantity() keine Exception wirft, ist die Menge gültig:
            self.products[product] = total_quantity

    def show(self):
        if not self.products:
            print("*** Your cart is empty!")
            return

        print("\n*** Your cart:")
        for product, quantity in self.products.items():
            print(
                f"{quantity:,.0f} {product.name} (${product.price:,.2f}) = ${product.price * quantity:,.2f}")

    def get_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_price() * quantity
        return total_price