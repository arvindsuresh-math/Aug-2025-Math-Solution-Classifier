def solve():
    """Index: 3881.
    Returns: the price per ounce in cents of the box with the better value.
    """
    # L1
    larger_box_cost_cents = 480 # The larger box costs $4.80 (converted to cents)
    larger_box_ounces = 30 # The larger box is 30 ounces
    larger_box_price_per_ounce = larger_box_cost_cents / larger_box_ounces

    # L2
    smaller_box_cost_cents = 340 # The smaller box costs $3.40 (converted to cents)
    smaller_box_ounces = 20 # the smaller box is 20 ounces
    smaller_box_price_per_ounce = smaller_box_cost_cents / smaller_box_ounces

    # L3
    better_value_price_per_ounce = min(larger_box_price_per_ounce, smaller_box_price_per_ounce)

    # FA
    answer = better_value_price_per_ounce
    return answer