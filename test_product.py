import pytest
from products import Product


# 1. Test that creating a normal product works.
def test_create_normal_product():
    product = Product("MacBook Pro", 1999.99, 10)

    assert product.name == "MacBook Pro"
    assert product.price == 1999.99
    assert product.get_quantity() == 10
    assert product.is_active() is True


# 2. Test that creating a product with invalid details invokes an exception.
def test_create_product_invalid_details():
    # Test empty name
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", 1450, 100)

    # Test negative price
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Product("MacBook Air M2", -10, 100)

    # Test zero price (as your __init__ says price <= 0 raises ValueError)
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Product("MacBook Air M2", 0, 100)

    # Test negative quantity
    with pytest.raises(ValueError, match="Quantity must be greater than 0"):
        Product("MacBook Air M2", 1450, -5)


# 3. Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_becomes_inactive():
    product = Product("Headphones", 150.0, 1)

    # Buy the last remaining item
    product.buy(1)

    assert product.get_quantity() == 0
    assert product.is_active() is False


# 4. Test that product purchase modifies the quantity and returns the right output.
def test_product_purchase():
    product = Product("Gaming Mouse", 50.0, 10)

    # Buy 3 items
    total_cost = product.buy(3)

    assert total_cost == 150.0
    assert product.get_quantity() == 7
    assert product.is_active() is True  # Should still be active


# 5. Test that buying a larger quantity than exists invokes exception.
def test_buy_exceeds_maximum_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=5)

    # Attempt to buy 6 items when only 5 exist
    with pytest.raises(ValueError, match="exceeds the maximum quantity"):
        product.buy(6)