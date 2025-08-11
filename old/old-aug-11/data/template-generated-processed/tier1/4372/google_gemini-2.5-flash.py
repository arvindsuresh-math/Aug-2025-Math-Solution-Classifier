def solve():
    """Index: 4372.
    Returns: the amount of money Cory needs to buy the candies.
    """
    # L1
    cost_per_pack = 49.00 # $49.00 each
    num_packs = 2 # two packs of candies
    total_cost_candies = cost_per_pack * num_packs

    # L2
    cory_has = 20.00 # $20.00
    money_needed = total_cost_candies - cory_has

    # FA
    answer = money_needed
    return answer