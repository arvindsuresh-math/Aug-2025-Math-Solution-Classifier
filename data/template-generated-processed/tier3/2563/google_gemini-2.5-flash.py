def solve():
    """Index: 2563.
    Returns: the number of cows that are not black.
    """
    # L1
    total_cows = 18 # Sam has 18 cows
    half_divisor = 2 # Half of the cows
    half_cows = total_cows / half_divisor

    # L2
    more_than_half = 5 # 5 more than half the cows
    black_cows = more_than_half + half_cows

    # L3
    not_black_cows = total_cows - black_cows

    # FA
    answer = not_black_cows
    return answer