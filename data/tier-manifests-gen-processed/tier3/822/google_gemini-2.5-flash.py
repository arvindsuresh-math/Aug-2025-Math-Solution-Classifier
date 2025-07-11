def solve():
    """Index: 822.
    Returns: the number of packs of 10 cupcakes Jean needs to buy.
    """
    # L1
    cupcakes_per_pack_15 = 15 # packages of 15
    packs_of_15_bought = 4 # bought 4 packs of 15 cupcakes
    cupcakes_from_15_packs = cupcakes_per_pack_15 * packs_of_15_bought

    # L2
    children_count = 100 # 100 children
    cupcakes_needed_more = children_count - cupcakes_from_15_packs

    # L3
    cupcakes_per_pack_10 = 10 # packages of 10
    packs_of_10_to_buy = cupcakes_needed_more / cupcakes_per_pack_10

    # FA
    answer = packs_of_10_to_buy
    return answer