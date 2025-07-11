def solve():
    """Index: 296.
    Returns: the number of kilos of sugar remaining.
    """
    # L1
    total_sugar = 24 # Chelsea has 24 kilos of sugar
    num_bags = 4 # divides them into 4 bags equally
    sugar_per_bag = total_sugar / num_bags

    # L2
    torn_fraction_denominator = 2 # half of the sugar falls
    sugar_lost = sugar_per_bag / torn_fraction_denominator

    # L3
    sugar_remaining = total_sugar - sugar_lost

    # FA
    answer = sugar_remaining
    return answer