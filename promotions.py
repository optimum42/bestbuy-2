from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract Base Class representing a general promotion.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Abstract method that must be overridden by child classes.
        Calculates the total price of the product after promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Applies a percentage discount to the entire quantity.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount_multiplier = 1 - (self.percent / 100)
        return (product.price * discount_multiplier) * quantity


class SecondHalfPrice(Promotion):
    """
    For every 2 items bought, the second one is at 50% off.
    (Effectively: Buy 2 items, pay for 1.5)
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        # Calculate how many pairs of 2 we have, and the remainder
        full_price_items = (quantity // 2) + (quantity % 2)
        half_price_items = quantity // 2

        return (full_price_items * product.price) + (
                    half_price_items * (product.price * 0.5))


class ThirdOneFree(Promotion):
    """
    For every 3 items bought, pay for 2. (Buy 2, get 1 free).
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        # Calculate how many groups of 3 we have
        free_items = quantity // 3
        payable_items = quantity - free_items

        return payable_items * product.price