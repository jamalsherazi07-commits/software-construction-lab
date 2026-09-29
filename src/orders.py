"""Order processing module for Lab 2."""

from typing import Any


def calculate_items_subtotal(items: list[dict[str, Any]]) -> float:
    """Calculate the subtotal for all items with positive price and quantity."""
    subtotal = 0.0
    for item in items:
        price = item["price"]
        quantity = item["qty"]
        if price <= 0 or quantity <= 0:
            continue
        subtotal += price * quantity
    return subtotal


def calculate_member_discount(subtotal: float, is_member: bool) -> float:
    """Calculate the discount amount for members based on subtotal tiers."""
    if not is_member:
        return 0.0
    if subtotal > 100:
        return subtotal * 0.2
    if subtotal > 50:
        return subtotal * 0.1
    return 0.0


def calculate_shipping_cost(country: str) -> float:
    """Calculate shipping cost based on the destination country."""
    if country == "PK":
        return 5.0
    if country == "US":
        return 15.0
    return 25.0


def calculate_order_total(order: dict[str, Any]) -> float:
    """Compose subtotal, member discount, and shipping cost into final total."""
    subtotal = calculate_items_subtotal(order["items"])
    discount = calculate_member_discount(subtotal, order["member"])
    shipping = calculate_shipping_cost(order["country"])
    return subtotal - discount + shipping
