def solve():
    """Index: 1773.
    Returns: the number of gifts Savannah wrapped with the third roll of paper.
    """
    # L1
    total_gifts = 12 # 12 gifts
    gifts_first_roll = 3 # 1 roll to wrap 3 gifts
    gifts_second_roll = 5 # 1 roll to wrap 5 other gifts
    gifts_wrapped_first_two = gifts_first_roll + gifts_second_roll

    # L2
    gifts_third_roll = total_gifts - gifts_wrapped_first_two

    # FA
    answer = gifts_third_roll
    return answer