def solve():
    """Index: 558.
    Returns: the total dollar value of gift cards Jack can still return.
    """
    # L1
    initial_best_buy_cards = 6 # 6 $500 Best Buy gift cards
    sent_best_buy_cards = 1 # 1 Best Buy gift card
    remaining_best_buy_cards = initial_best_buy_cards - sent_best_buy_cards

    # L2
    cost_per_best_buy_card = 500 # $500 Best Buy gift cards
    refund_best_buy = remaining_best_buy_cards * cost_per_best_buy_card

    # L3
    initial_walmart_cards = 9 # 9 $200 Walmart gift cards
    sent_walmart_cards = 2 # 2 Walmart gift cards
    remaining_walmart_cards = initial_walmart_cards - sent_walmart_cards

    # L4
    cost_per_walmart_card = 200 # $200 Walmart gift cards
    refund_walmart = remaining_walmart_cards * cost_per_walmart_card

    # L5
    total_refund = refund_best_buy + refund_walmart

    # FA
    answer = total_refund
    return answer