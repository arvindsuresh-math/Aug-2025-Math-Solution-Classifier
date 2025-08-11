def solve():
    """Index: 1438.
    Returns: the weight of the soup on the fourth day.
    """
    # L1
    initial_weight = 80 # weighing 80 kg
    reduction_divisor = 2 # reduced by half
    weight_day1 = initial_weight / reduction_divisor

    # L2
    weight_day2 = weight_day1 / reduction_divisor

    # L3
    weight_day3 = weight_day2 / reduction_divisor

    # L4
    weight_day4 = weight_day3 / reduction_divisor

    # FA
    answer = weight_day4
    return answer