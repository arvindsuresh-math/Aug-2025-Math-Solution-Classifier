def solve():
    """Index: 640.
    Returns: the number of ceilings left to paint after next week.
    """
    # L1
    total_ceilings = 28 # Michelangelo has 28 ceilings to paint
    painted_this_week = 12 # he paints 12 of them
    remaining_after_this_week = total_ceilings - painted_this_week

    # L2
    fraction_denominator = 4 # 1/4 the number of ceilings
    painted_next_week = painted_this_week / fraction_denominator

    # L3
    remaining_after_next_week = remaining_after_this_week - painted_next_week

    # FA
    answer = remaining_after_next_week
    return answer