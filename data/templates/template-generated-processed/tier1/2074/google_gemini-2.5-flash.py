def solve():
    """Index: 2074.
    Returns: the price of the gift.
    """
    # L1
    guest_contribution = 5 # $5 for this purpose
    num_guests = 12 # 12 guests invited
    money_from_guests = guest_contribution * num_guests

    # L2
    samanta_contribution = 10 # she herself put in $10
    total_money_collected = money_from_guests + samanta_contribution

    # L3
    leftover_money = 15 # $15 leftover
    gift_price = total_money_collected - leftover_money

    # FA
    answer = gift_price
    return answer