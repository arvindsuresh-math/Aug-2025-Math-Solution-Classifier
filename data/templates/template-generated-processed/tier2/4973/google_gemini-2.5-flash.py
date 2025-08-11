def solve():
    """Index: 4973.
    Returns: the total pounds of fish caught.
    """
    # L1
    trout_pounds = 200 # 200 pounds of trout
    salmon_increase_factor = 0.55 # from solution calculation 200*.55
    salmon_increase_pounds = trout_pounds * salmon_increase_factor

    # L2
    salmon_total_pounds = trout_pounds + salmon_increase_pounds

    # L3
    tuna_multiplier = 2 # twice as much Tuna
    tuna_pounds = salmon_total_pounds * tuna_multiplier

    # L4
    total_fish_pounds = tuna_pounds + salmon_total_pounds + trout_pounds

    # FA
    answer = total_fish_pounds
    return answer