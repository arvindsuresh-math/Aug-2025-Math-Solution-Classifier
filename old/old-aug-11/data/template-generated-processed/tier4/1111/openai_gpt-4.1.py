def solve():
    """Index: 1111.
    Returns: the total amount Barbara spent at the butchers.
    """
    # L1
    num_steaks = 4 # 4 steaks
    steak_weight_each = 0.5 # 1/2 pound steaks
    total_steak_weight = num_steaks * steak_weight_each

    # L2
    steak_price_per_pound = 15 # $15.00/pound
    steak_total_cost = steak_price_per_pound * total_steak_weight

    # L3
    chicken_weight = 1.5 # 1.5 pounds of chicken breasts
    chicken_price_per_pound = 8 # $8.00 a pound
    chicken_total_cost = chicken_weight * chicken_price_per_pound

    # L4
    total_cost = steak_total_cost + chicken_total_cost

    # FA
    answer = total_cost
    return answer