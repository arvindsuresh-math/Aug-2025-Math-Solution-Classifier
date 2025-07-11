def solve():
    """Index: 1111.
    Returns: the total amount spent at the butchers.
    """
    # L1
    num_steaks = 4 # 4 1/2 pound steaks
    steak_weight_per_steak = 0.5 # 1/2 pound steaks
    total_steak_pounds = num_steaks * steak_weight_per_steak

    # L2
    steak_cost_per_pound = 15.00 # $15.00/pound
    total_steak_cost = steak_cost_per_pound * total_steak_pounds

    # L3
    chicken_pounds = 1.5 # a pound and half of chicken breasts
    chicken_cost_per_pound = 8.00 # $8.00 a pound
    total_chicken_cost = chicken_pounds * chicken_cost_per_pound

    # L4
    total_spent = total_steak_cost + total_chicken_cost

    # FA
    answer = total_spent
    return answer