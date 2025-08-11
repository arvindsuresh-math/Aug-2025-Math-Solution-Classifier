def solve():
    """Index: 2074.
    Returns: the price of the gift Samanta bought for Marta.
    """
    # L1
    amount_per_guest = 5 # Every participant gave Samanta $5
    num_guests = 12 # 12 guests invited
    total_from_guests = amount_per_guest * num_guests

    # L2
    samanta_contribution = 10 # she herself put in $10
    total_money = total_from_guests + samanta_contribution

    # L3
    leftover = 15 # there was $15 leftover
    gift_price = total_money - leftover

    # FA
    answer = gift_price
    return answer