def solve():
    """Index: 5598.
    Returns: the total weight of Frances's towels in ounces.
    """
    # L1
    mary_towels = 24 # Mary has 24 towels
    mary_towels_multiplier = 4 # 4 times as many towels as Frances does
    frances_towels = mary_towels / mary_towels_multiplier

    # L2
    total_towels = mary_towels + frances_towels

    # L3
    total_weight_pounds = 60 # The total weight of their towels is 60 pounds
    weight_per_towel_pounds = total_weight_pounds / total_towels

    # L4
    frances_towels_weight_pounds = weight_per_towel_pounds * mary_towels_multiplier

    # L5
    ounces_per_pound = 16 # WK
    frances_towels_weight_ounces = frances_towels_weight_pounds * ounces_per_pound

    # FA
    answer = frances_towels_weight_ounces
    return answer