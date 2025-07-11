from fractions import Fraction

def solve():
    """Index: 1075.
    Returns: the total amount Celina spent on equipment.
    """
    # L1
    hoodie_cost = 80 # The hoodie cost $80
    flashlight_percentage = Fraction(20, 100) # 20% of that price
    flashlight_cost = hoodie_cost * flashlight_percentage

    # L2
    original_boots_cost = 110 # The pair of boots cost was $110
    promotion_percentage = Fraction(10, 100) # 10% cheaper
    promotion_discount = original_boots_cost * promotion_percentage

    # L3
    final_boots_cost = original_boots_cost - promotion_discount

    # L4
    total_spent = hoodie_cost + flashlight_cost + final_boots_cost

    # FA
    answer = total_spent
    return answer