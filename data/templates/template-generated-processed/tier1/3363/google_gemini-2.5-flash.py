def solve():
    """Index: 3363.
    Returns: the total number of Joseph's socks.
    """
    # L1
    red_socks = 6 # counted a total of 6 red socks
    multiplier_blue_red = 2 # twice as many blue socks as he had of red socks
    blue_socks = multiplier_blue_red * red_socks

    # L2
    red_socks_less_than_white_pairs = 1 # one less pair of red socks than he had pairs of white socks
    socks_per_pair = 2 # WK
    fewer_red_socks_than_white = red_socks_less_than_white_pairs * socks_per_pair
    white_socks = red_socks - fewer_red_socks_than_white

    # L3
    blue_socks_pairs = blue_socks / socks_per_pair

    # L4
    blue_socks_more_than_black_pairs = 3 # three more pairs of blue socks than pairs of black socks
    black_socks_pairs = blue_socks_pairs - blue_socks_more_than_black_pairs

    # L5
    black_socks = black_socks_pairs * socks_per_pair

    # L6
    total_socks = red_socks + blue_socks + white_socks + black_socks

    # FA
    answer = total_socks
    return answer