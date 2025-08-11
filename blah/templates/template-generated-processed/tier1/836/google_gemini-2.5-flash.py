def solve():
    """Index: 836.
    Returns: the difference between the number of tails and heads.
    """
    # L1
    total_flips = 211 # 211 times
    heads_flips = 65 # 65 of the flips
    tails_flips = total_flips - heads_flips

    # L2
    more_tails_than_heads = tails_flips - heads_flips

    # FA
    answer = more_tails_than_heads
    return answer