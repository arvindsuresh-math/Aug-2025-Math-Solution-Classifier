def solve():
    """Index: 296.
    Returns: the number of kilos of sugar that remain after the accident.
    """
    # L1
    total_sugar = 24 # Chelsea has 24 kilos of sugar
    num_bags = 4 # divides them into 4 bags equally
    sugar_per_bag = total_sugar / num_bags

    # L2
    half = 2 # half of the sugar falls to the ground
    sugar_fallen = sugar_per_bag / half

    # L3
    sugar_remaining = total_sugar - sugar_fallen

    # FA
    answer = sugar_remaining
    return answer