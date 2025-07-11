def solve():
    """Index: 1773.
    Returns: the number of gifts wrapped with the third roll of paper.
    """
    # L1
    gifts_wrapped_roll1 = 3 # 1 roll to wrap 3 gifts
    gifts_wrapped_roll2 = 5 # 1 roll to wrap 5 other gifts
    gifts_wrapped_first_two_rolls = gifts_wrapped_roll1 + gifts_wrapped_roll2

    # L2
    total_gifts = 12 # 12 gifts
    gifts_wrapped_third_roll = total_gifts - gifts_wrapped_first_two_rolls

    # FA
    answer = gifts_wrapped_third_roll
    return answer