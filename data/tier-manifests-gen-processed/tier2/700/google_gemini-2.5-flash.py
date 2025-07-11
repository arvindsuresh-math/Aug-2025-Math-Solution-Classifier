def solve():
    """Index: 700.
    Returns: the total cost for 15 brown socks.
    """
    # L1
    cost_two_white_socks = 0.45 # If two white socks cost 45 cents
    price_difference = 0.25 # 25 cents more
    cost_single_brown_sock = cost_two_white_socks - price_difference

    # L2
    num_brown_socks = 15 # 15 brown socks
    total_cost_brown_socks = num_brown_socks * cost_single_brown_sock

    # FA
    answer = total_cost_brown_socks
    return answer