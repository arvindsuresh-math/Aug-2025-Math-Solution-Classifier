def solve():
    """Index: 6076.
    Returns: the number of cows the farmer has left.
    """
    # L1
    initial_cows = 51 # A farmer has 51 cows
    added_cows = 5 # adds five new cows
    total_cows_after_addition = initial_cows + added_cows

    # L2
    quarter_divisor = 4 # sells a quarter of the herd
    cows_sold = total_cows_after_addition / quarter_divisor

    # L3
    remaining_cows = total_cows_after_addition - cows_sold

    # FA
    answer = remaining_cows
    return answer