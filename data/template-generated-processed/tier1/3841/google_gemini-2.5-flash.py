def solve():
    """Index: 3841.
    Returns: the amount of change Laura received.
    """
    # L1
    price_per_pant_pair = 54 # 2 pairs of pants for $54 each
    num_pant_pairs = 2 # 2 pairs of pants
    price_of_pants = price_per_pant_pair * num_pant_pairs

    # L2
    num_shirts = 4 # 4 shirts
    price_per_shirt = 33 # 4 shirts for $33 each
    price_of_shirts = num_shirts * price_per_shirt

    # L3
    total_price = price_of_pants + price_of_shirts

    # L4
    amount_given_to_cashier = 250 # gave $250 to the cashier
    change = amount_given_to_cashier - total_price

    # FA
    answer = change
    return answer