def solve():
    """Index: 4321.
    Returns: the number of jellybeans Tino has.
    """
    # L1
    arnold_jellybeans = 5 # Arnold has 5 jellybeans
    half_multiplier = 2 # half as many jellybeans as Lee
    lee_jellybeans = arnold_jellybeans * half_multiplier

    # L2
    tino_more_than_lee = 24 # 24 more jellybeans than Lee
    tino_jellybeans = lee_jellybeans + tino_more_than_lee

    # FA
    answer = tino_jellybeans
    return answer