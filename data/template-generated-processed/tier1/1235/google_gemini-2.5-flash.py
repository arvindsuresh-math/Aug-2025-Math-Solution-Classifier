def solve():
    """Index: 1235.
    Returns: the amount of money Penny has left.
    """
    # L1
    num_pairs_socks = 4 # 4 pairs of socks
    cost_per_pair = 2 # $2 a pair
    cost_socks = cost_per_pair * num_pairs_socks

    # L2
    cost_hat = 7 # a hat for $7
    total_spent = cost_socks + cost_hat

    # L3
    initial_money = 20 # Penny has $20
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer