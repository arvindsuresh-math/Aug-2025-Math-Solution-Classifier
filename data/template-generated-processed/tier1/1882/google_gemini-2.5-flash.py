def solve():
    """Index: 1882.
    Returns: the initial number of bananas on the tree.
    """
    # L1
    eaten_bananas_in_basket = 70 # Raj has eaten 70 bananas
    multiplier_for_remaining = 2 # has twice as many remaining in his basket
    remaining_bananas_in_basket = multiplier_for_remaining * eaten_bananas_in_basket

    # L2
    total_cut_bananas = remaining_bananas_in_basket + eaten_bananas_in_basket

    # L3
    bananas_left_on_tree = 100 # 100 bananas left after Raj cut some bananas from it
    initial_bananas_on_tree = bananas_left_on_tree + total_cut_bananas

    # FA
    answer = initial_bananas_on_tree
    return answer