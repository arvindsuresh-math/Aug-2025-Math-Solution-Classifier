def solve():
    """Index: 2663.
    Returns: the number of dollars of profit Nicky makes from the trade.
    """
    # L1
    value_per_card = 8 # $8 each
    num_cards_given = 2 # two cards
    total_given = value_per_card * num_cards_given

    # L2
    value_received = 21 # 1 card worth $21
    profit = value_received - total_given

    # FA
    answer = profit
    return answer