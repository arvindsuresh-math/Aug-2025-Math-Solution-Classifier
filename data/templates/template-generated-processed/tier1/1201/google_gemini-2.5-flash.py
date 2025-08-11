def solve():
    """Index: 1201.
    Returns: the amount of money Betty will pay for the packs of nuts.
    """
    # L1
    sum_ages = 90 # the sum of their ages is 90
    doug_age = 40 # Doug, Betty's friend, is 40 years old
    betty_age = sum_ages - doug_age

    # L2
    twice_multiplier = 2 # Twice Betty's age
    cost_per_pack = twice_multiplier * betty_age

    # L3
    num_packs_to_buy = 20 # buy 20 packs of the nuts
    total_cost = num_packs_to_buy * cost_per_pack

    # FA
    answer = total_cost
    return answer