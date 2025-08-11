def solve():
    """Index: 705.
    Returns: the initial amount of money Isabel had.
    """
    # L1
    money_left_after_book = 51 # If she has $51 left
    multiplier_for_half = 2 # WK
    money_before_book = money_left_after_book * multiplier_for_half

    # L2
    money_before_toy = money_before_book * multiplier_for_half

    # FA
    answer = money_before_toy
    return answer