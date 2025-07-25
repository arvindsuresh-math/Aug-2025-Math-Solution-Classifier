def solve():
    """Index: 2663.
    Returns: the profit Nicky makes in dollars.
    """
    # L1
    card_value_traded = 8 # two cards worth $8 each
    num_cards_traded = 2 # two cards
    total_cost_traded = card_value_traded * num_cards_traded

    # L2
    card_value_received = 21 # 1 card worth $21
    profit = card_value_received - total_cost_traded

    # FA
    answer = profit
    return answer