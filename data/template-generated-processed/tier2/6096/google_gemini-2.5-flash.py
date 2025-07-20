def solve():
    """Index: 6096.
    Returns: how much steak John ate.
    """
    # L1
    original_steak_weight = 30 # originally 30 ounces
    burned_fraction = 0.5 # burns half his steak
    unburnt_steak_weight = original_steak_weight * burned_fraction

    # L2
    eaten_percentage = 0.8 # eats 80% of what isn't burned
    eaten_steak_weight = unburnt_steak_weight * eaten_percentage

    # FA
    answer = eaten_steak_weight
    return answer