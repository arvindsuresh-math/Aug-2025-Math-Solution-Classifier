def solve():
    """Index: 3688.
    Returns: the total number of points Noa and Phillip scored to win the bowl.
    """
    # L1
    noa_score = 30 # Noa scored 30 points
    multiplier_for_philip = 2 # twice that number
    philip_score = multiplier_for_philip * noa_score

    # L2
    total_score = philip_score + noa_score

    # FA
    answer = total_score
    return answer