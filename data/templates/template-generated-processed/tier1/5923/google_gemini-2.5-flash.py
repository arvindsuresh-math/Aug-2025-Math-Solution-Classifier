def solve():
    """Index: 5923.
    Returns: the number of fireflies remaining.
    """
    # L1
    dozen = 12 # WK
    less_than_dozen = 4 # four less than a dozen more fireflies
    four_less_than_dozen = dozen - less_than_dozen

    # L2
    initial_fireflies = 3 # three fireflies danced
    total_after_joined = initial_fireflies + four_less_than_dozen

    # L3
    flew_away = 2 # two of the fireflies flew away
    fireflies_remaining = total_after_joined - flew_away

    # FA
    answer = fireflies_remaining
    return answer