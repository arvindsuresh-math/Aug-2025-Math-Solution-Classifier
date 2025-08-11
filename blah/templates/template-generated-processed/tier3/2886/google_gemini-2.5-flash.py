def solve():
    """Index: 2886.
    Returns: the total number of stairs Veronica and Samir climbed together.
    """
    # L1
    samir_stairs = 318 # Samir climbed 318 stairs yesterday
    half_divisor = 2 # Half of 318
    half_samir_stairs = samir_stairs / half_divisor

    # L2
    more_than_half = 18 # 18 more than half that amount
    veronica_stairs = half_samir_stairs + more_than_half

    # L3
    total_stairs = samir_stairs + veronica_stairs

    # FA
    answer = total_stairs
    return answer