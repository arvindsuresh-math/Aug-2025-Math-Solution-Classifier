def solve():
    """Index: 1201.
    Returns: the total amount of money Betty will pay for 20 packs of nuts.
    """
    # L1
    sum_ages = 90 # the sum of their ages is 90
    doug_age = 40 # Doug ... is 40 years old
    betty_age = sum_ages - doug_age

    # L2
    multiplier_for_cost = 2 # Twice Betty's age is the cost of a pack of nuts
    cost_per_pack = multiplier_for_cost * betty_age

    # L3
    packs_to_buy = 20 # Betty wants to buy 20 packs
    total_cost = packs_to_buy * cost_per_pack

    # FA
    answer = total_cost
    return answer