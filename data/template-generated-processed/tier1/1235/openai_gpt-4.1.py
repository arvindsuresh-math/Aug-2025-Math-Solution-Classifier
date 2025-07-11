def solve():
    """Index: 1235.
    Returns: the amount of money Penny has left after her purchases.
    """
    # L1
    num_pairs_socks = 4 # 4 pairs of socks
    price_per_pair = 2 # $2 a pair
    socks_total = num_pairs_socks * price_per_pair

    # L2
    hat_price = 7 # a hat for $7
    total_spent = socks_total + hat_price

    # L3
    initial_money = 20 # Penny has $20
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer