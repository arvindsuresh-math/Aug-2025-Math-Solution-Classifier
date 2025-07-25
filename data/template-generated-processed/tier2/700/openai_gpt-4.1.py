def solve():
    """Index: 700.
    Returns: the total cost for 15 brown socks.
    """
    # L1
    two_white_cost = 0.45 # two white socks cost 45 cents
    price_difference = 0.25 # 25 cents more than a single brown sock
    brown_sock_cost = two_white_cost - price_difference

    # L2
    num_brown_socks = 15 # 15 brown socks
    total_brown_cost = num_brown_socks * brown_sock_cost

    # FA
    answer = total_brown_cost
    return answer