from fractions import Fraction

def solve():
    """Index: 5625.
    Returns: the total cost Hannah would pay for apples.
    """
    # L1
    discount_percentage = Fraction(40, 100) # 40% discount
    price_per_kg = 5 # $5 per kilogram
    discount_amount_per_kg = discount_percentage * price_per_kg

    # L2
    discounted_price_per_kg = price_per_kg - discount_amount_per_kg

    # L3
    quantity_kg = 10 # 10 kilograms of them
    total_cost = discounted_price_per_kg * quantity_kg

    # FA
    answer = total_cost
    return answer