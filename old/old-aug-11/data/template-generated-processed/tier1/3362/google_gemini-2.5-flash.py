def solve():
    """Index: 3362.
    Returns: the maximum combined weight the flock can carry.
    """
    # L3
    total_flock_size = 90 # flock of 90 swallows
    american_to_european_ratio = 2 # containing twice as many American as European swallows
    coefficient_for_x = american_to_european_ratio + 1
    num_european_swallows = total_flock_size / coefficient_for_x

    # L4
    num_american_swallows = total_flock_size - num_european_swallows

    # L5
    american_swallow_max_weight = 5 # maximum of 5 pounds of weight
    european_carry_multiplier = 2 # twice the weight as the American swallow
    european_swallow_carry_capacity = european_carry_multiplier * american_swallow_max_weight

    # L6
    total_european_carry_capacity = num_european_swallows * european_swallow_carry_capacity

    # L7
    total_american_carry_capacity = num_american_swallows * american_swallow_max_weight

    # L8
    total_flock_carry_capacity = total_european_carry_capacity + total_american_carry_capacity

    # FA
    answer = total_flock_carry_capacity
    return answer