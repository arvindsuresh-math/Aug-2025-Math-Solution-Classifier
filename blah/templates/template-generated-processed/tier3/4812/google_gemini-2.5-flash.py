def solve():
    """Index: 4812.
    Returns: the total number of dinners sold in 4 days.
    """
    # L1
    dinners_monday = 40 # forty dinners
    more_dinners_tuesday = 40 # 40 more dinners than it did Monday
    dinners_tuesday = dinners_monday + more_dinners_tuesday

    # L2
    half_divisor = 2 # half the amount of dinners
    dinners_wednesday = dinners_tuesday / half_divisor

    # L3
    additional_dinners_thursday = 3 # 3 more dinners
    dinners_thursday = dinners_wednesday + additional_dinners_thursday

    # L4
    total_dinners_4_days = dinners_monday + dinners_tuesday + dinners_wednesday + dinners_thursday

    # FA
    answer = total_dinners_4_days
    return answer