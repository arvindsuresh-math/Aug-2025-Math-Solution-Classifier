def solve():
    """Index: 6336.
    Returns: the number of new cards Marco got.
    """
    # L1
    total_cards = 500 # total of 500 cards
    duplicate_fraction = 0.25 # a fourth of them are duplicates
    duplicate_cards = total_cards * duplicate_fraction

    # L2
    trade_fraction = 0.2 # one-fifth of these duplicates
    new_cards = duplicate_cards * trade_fraction

    # FA
    answer = new_cards
    return answer