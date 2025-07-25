def solve():
    """Index: 6967.
    Returns: the total number of pencils Anika and Reeta have together.
    """
    # L1
    reeta_pencils = 20 # Reeta has 20 pencils
    multiplier_twice = 2 # twice the number
    twice_reeta_pencils = multiplier_twice * reeta_pencils

    # L2
    anika_more_than_twice = 4 # 4 more than twice the number
    anika_pencils = twice_reeta_pencils + anika_more_than_twice

    # L3
    total_pencils = anika_pencils + reeta_pencils

    # FA
    answer = total_pencils
    return answer