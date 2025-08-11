def solve():
    """Index: 558.
    Returns: the total dollar value of gift cards Jack can still return.
    """
    # L1
    bestbuy_total_cards = 6 # 6 $500 Best Buy gift cards
    bestbuy_sent_cards = 1 # codes for 1 Best Buy gift card
    bestbuy_remaining_cards = bestbuy_total_cards - bestbuy_sent_cards

    # L2
    bestbuy_card_value = 500 # $500 Best Buy gift cards
    bestbuy_refund = bestbuy_remaining_cards * bestbuy_card_value

    # L3
    walmart_total_cards = 9 # 9 $200 Walmart gift cards
    walmart_sent_cards = 2 # codes for 2 Walmart gift cards
    walmart_remaining_cards = walmart_total_cards - walmart_sent_cards

    # L4
    walmart_card_value = 200 # $200 Walmart gift cards
    walmart_refund = walmart_remaining_cards * walmart_card_value

    # L5
    total_refund = bestbuy_refund + walmart_refund

    # FA
    answer = total_refund
    return answer