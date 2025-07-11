def solve():
    """Index: 1607.
    Returns: the amount of money Jean has.
    """
    # L5
    combined_total_money = 76 # They have a combined total of $76
    jean_multiplier = 3 # three times as much money as Jane
    jane_multiplier = 1 # WK
    total_parts = jane_multiplier + jean_multiplier
    jane_money = combined_total_money / total_parts

    # L7
    jean_money = jean_multiplier * jane_money

    # FA
    answer = jean_money
    return answer