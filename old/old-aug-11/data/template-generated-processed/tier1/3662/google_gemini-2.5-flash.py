def solve():
    """Index: 3662.
    Returns: the number of additional packs of cookies Tory needs to sell.
    """
    # L1
    grandmother_packs = 12 # sold 12 packs to his grandmother
    uncle_packs = 7 # 7 packs to his uncle
    sold_to_family = grandmother_packs + uncle_packs

    # L2
    neighbor_packs = 5 # 5 packs to a neighbor
    total_sold = sold_to_family + neighbor_packs

    # L3
    target_packs = 50 # sell 50 packs of cookies
    packs_needed = target_packs - total_sold

    # FA
    answer = packs_needed
    return answer