import products

class Store:
    """
    The store class that holds all products
    It allows the user to add, remove, and order products
    """
    def __init__(self, store_name, product_list):
        self.name = store_name
        self.product_list = product_list

    def __contains__(self, product):
        """
        Allows using the 'in' operator to check if a product is in the store.
        """
        return product in self.product_list

    def __add__(self, other):
        """
        Allows using the '+' operator to combine two stores.
        Returns a new Store instance containing products from both.
        """
        if not isinstance(other, Store):
            return NotImplemented

        # Create a combined name for the new mega-store
        new_store_name = f"{self.name} & {other.name}"

        # Combine the product lists
        combined_products = self.product_list + other.product_list

        return Store(new_store_name, combined_products)

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        return [product for product in self.product_list if product.is_active()]

    def order(self, cart):
        total_amount = 0
        for product, quantity in cart.products.items():

            if product not in self:
                raise ValueError(
                    f"{product.name}: Product does not belong to this store")

            if not product.is_active():
                raise ValueError(
                    f"{product.name}: Product currently not available")

            total_amount += product.buy(quantity)

        return total_amount


def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store("Best Buy", product_list)
    all_products = best_buy.get_all_products()

    print("Available products\n--------------------------")
    for product in all_products:
        print(product)
    print(f"Total quantity: {best_buy.get_total_quantity()}")

    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    best_buy2 = Store("Test Buy", [mac])
    print(mac)
    if mac in best_buy2:
        print("Yes, this store carries the MacBook Air!")
    else:
        print("No, this store has no MacBook Air!")


if __name__ == "__main__":
    main()