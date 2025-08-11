def solve():
    """Index: 6962.
    Returns: the total amount of money Keanu spent on fish.
    """
    # L1
    dog_fish = 40 # he gave his dog 40 fish
    cat_fraction_numerator = 1 # half as many fish
    cat_fraction_denominator = 2 # half as many fish
    cat_fish = (cat_fraction_numerator / cat_fraction_denominator) * dog_fish

    # L2
    total_fish = cat_fish + dog_fish

    # L3
    cost_per_fish = 4 # each fish cost him $4
    total_cost = total_fish * cost_per_fish

    # FA
    answer = total_cost
    return answer