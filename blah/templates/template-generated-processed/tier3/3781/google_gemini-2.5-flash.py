def solve():
    """Index: 3781.
    Returns: the number of blue socks Joan has.
    """
    # L1
    total_socks = 180 # Joan has 180 socks
    white_socks_denominator = 3 # Two thirds of the socks
    white_socks_numerator = 2 # Two thirds of the socks
    white_socks = (total_socks / white_socks_denominator) * white_socks_numerator

    # L2
    blue_socks = total_socks - white_socks

    # FA
    answer = blue_socks
    return answer