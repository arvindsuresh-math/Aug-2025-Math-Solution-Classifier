def solve():
    """Index: 836.
    Returns: how many more tails than heads the solver got.
    """
    # L1
    total_flips = 211 # flips a coin 211 times
    num_heads = 65 # gets a head on 65 of the flips
    num_tails = total_flips - num_heads

    # L2
    more_tails_than_heads = num_tails - num_heads

    # FA
    answer = more_tails_than_heads
    return answer