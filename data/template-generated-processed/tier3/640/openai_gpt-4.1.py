def solve():
    """Index: 640.
    Returns: the number of ceilings Michelangelo will have left to paint after next week.
    """
    # L1
    total_ceilings = 28 # Michelangelo has 28 ceilings to paint
    ceilings_painted_this_week = 12 # he paints 12 of them
    ceilings_left_after_this_week = total_ceilings - ceilings_painted_this_week

    # L2
    next_week_divisor = 4 # 1/4 the number of ceilings he did this week
    ceilings_painted_next_week = ceilings_painted_this_week / next_week_divisor

    # L3
    ceilings_left_after_next_week = ceilings_left_after_this_week - ceilings_painted_next_week

    # FA
    answer = ceilings_left_after_next_week
    return answer