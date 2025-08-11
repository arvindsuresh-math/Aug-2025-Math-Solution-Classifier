def solve():
    """Index: 7331.
    Returns: the amount of pesetas saved by buying a big bottle instead of smaller bottles.
    """
    # L1
    big_bottle_volume = 30 # The big bottles of mango juice hold 30 ounces
    small_bottle_volume = 6 # The small bottles hold 6 ounces
    num_small_bottles_equivalent = big_bottle_volume / small_bottle_volume

    # L2
    small_bottle_cost = 600 # cost 600 pesetas each
    cost_of_equivalent_small_bottles = num_small_bottles_equivalent * small_bottle_cost

    # L3
    big_bottle_cost = 2700 # cost 2700 pesetas each
    savings = cost_of_equivalent_small_bottles - big_bottle_cost

    # FA
    answer = savings
    return answer