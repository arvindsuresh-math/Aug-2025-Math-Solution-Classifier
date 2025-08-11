def solve():
    """Index: 4238.
    Returns: the cost of Luca's drink in dollars.
    """
    # L1
    normal_sandwich_price = 8 # normally $8
    coupon_divisor = 4 # a quarter of the price off
    coupon_savings = normal_sandwich_price / coupon_divisor

    # L2
    avocado_cost = 1 # for an extra dollar
    sandwich_cost_after_discount_and_upgrade = normal_sandwich_price - coupon_savings + avocado_cost

    # L3
    salad_cost = 3 # a $3 salad
    meal_cost_without_drink = sandwich_cost_after_discount_and_upgrade + salad_cost

    # L4
    total_bill = 12 # his total lunch bill was $12
    drink_cost = total_bill - meal_cost_without_drink

    # FA
    answer = drink_cost
    return answer