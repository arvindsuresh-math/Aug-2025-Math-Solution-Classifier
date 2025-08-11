def solve():
    """Index: 6409.
    Returns: the total number of socks James has combined.
    """
    # L1
    red_socks_count = 20 # 20 pairs of red socks
    half_divisor = 2 # half as many black socks
    black_socks = red_socks_count / half_divisor

    # L2
    red_and_black_socks = red_socks_count + black_socks

    # L3
    white_socks_multiplier = 2 # twice as many white socks
    white_socks = red_and_black_socks * white_socks_multiplier

    # L4
    total_socks = white_socks + red_and_black_socks

    # FA
    answer = total_socks
    return answer