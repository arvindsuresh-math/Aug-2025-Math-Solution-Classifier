def solve():
    """Index: 5691.
    Returns: the total amount Arthur spent on dinner, including the tip.
    """
    # L1
    appetizer_cost = 8 # ordered a nice appetizer for $8
    ribeye_cost = 20 # a delicious ribeye steak for his entrée at $20
    wine_glass_cost = 3 # two glasses of nice red wine with dinner for $3 each
    cheesecake_cost = 6 # a slice of caramel cheesecake for dessert for $6
    full_meal_cost_before_voucher = appetizer_cost + ribeye_cost + wine_glass_cost + wine_glass_cost + cheesecake_cost

    # L2
    tip_percentage = 0.20 # tipped his waitress a full 20%
    tip_amount = full_meal_cost_before_voucher * tip_percentage

    # L3
    voucher_discount_divisor = 2 # voucher for half off the price of his entrée
    voucher_savings = ribeye_cost / voucher_discount_divisor

    # L4
    total_spent = full_meal_cost_before_voucher - voucher_savings + tip_amount

    # FA
    answer = total_spent
    return answer