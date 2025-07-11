def solve():
    """Index: 737.
    Returns: the total worth of all the packs of crayons Michael will have after the purchase.
    """
    # L1
    initial_packs = 4 # Michael has 4 packs of crayons
    packs_to_buy = 2 # wants to buy 2 more
    total_packs = initial_packs + packs_to_buy

    # L2
    pack_price = 2.5 # One pack of crayons costs $2.5
    total_worth = total_packs * pack_price

    # FA
    answer = total_worth
    return answer