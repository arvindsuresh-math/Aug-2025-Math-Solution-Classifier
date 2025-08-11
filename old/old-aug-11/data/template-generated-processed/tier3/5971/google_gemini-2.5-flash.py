def solve():
    """Index: 5971.
    Returns: the total money Matt can save.
    """
    # L1
    cost_pack_10 = 20 # packs of 10 for $20
    quantity_pack_10 = 10 # packs of 10
    cost_per_keychain_pack_10 = cost_pack_10 / quantity_pack_10

    # L2
    cost_pack_4 = 12 # packs of 4 for $12
    quantity_pack_4 = 4 # packs of 4
    cost_per_keychain_pack_4 = cost_pack_4 / quantity_pack_4

    # L3
    price_difference_per_keychain = cost_per_keychain_pack_4 - cost_per_keychain_pack_10

    # L4
    num_keychains_to_buy = 20 # buy 20 key chains
    total_savings = num_keychains_to_buy * price_difference_per_keychain

    # FA
    answer = total_savings
    return answer