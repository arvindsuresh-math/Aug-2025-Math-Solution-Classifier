def solve():
    """Index: 1045.
    Returns: the number of more white socks than black socks Andy has.
    """
    # L1
    black_socks = 6 # he has 6 black socks
    white_socks_multiplier = 4 # 4 times as many white socks
    initial_white_socks = black_socks * white_socks_multiplier

    # L2
    half_divisor = 2 # loses half his white socks
    remaining_white_socks = initial_white_socks / half_divisor

    # L3
    more_white_than_black = remaining_white_socks - black_socks

    # FA
    answer = more_white_than_black
    return answer