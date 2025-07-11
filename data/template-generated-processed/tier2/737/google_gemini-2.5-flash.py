def solve():
    """Index: 737.
    Returns: the total worth of all the crayon packs Michael will have.
    """
    # L1
    initial_packs = 4 # Michael has 4 packs of crayons
    packs_to_buy = 2 # wants to buy 2 more
    total_packs = initial_packs + packs_to_buy

    # L2
    cost_per_pack = 2.5 # One pack of crayons costs $2.5
    total_worth = total_packs * cost_per_pack

    # FA
    answer = total_worth
    return answer