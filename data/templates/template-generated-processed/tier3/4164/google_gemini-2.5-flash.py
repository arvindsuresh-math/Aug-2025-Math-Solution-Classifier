from fractions import Fraction

def solve():
    """Index: 4164.
    Returns: the total price of two kilograms of tomatoes and three kilograms of cucumbers.
    """
    # L1
    cheaper_percentage = Fraction(20, 100) # 20% cheaper
    cucumber_cost_per_kg = 5 # One kilogram of cucumbers costs $5
    tomato_discount_per_kg = cheaper_percentage * cucumber_cost_per_kg

    # L2
    tomato_cost_per_kg = cucumber_cost_per_kg - tomato_discount_per_kg

    # L3
    quantity_tomatoes = 2 # two kilograms of tomatoes
    total_cost_tomatoes = quantity_tomatoes * tomato_cost_per_kg

    # L4
    quantity_cucumbers = 3 # three kilograms of cucumbers
    total_cost_cucumbers = quantity_cucumbers * cucumber_cost_per_kg

    # L5
    total_price_both_products = total_cost_tomatoes + total_cost_cucumbers

    # FA
    answer = total_price_both_products
    return answer