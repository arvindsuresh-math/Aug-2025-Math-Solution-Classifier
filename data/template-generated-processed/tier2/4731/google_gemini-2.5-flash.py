def solve():
    """Index: 4731.
    Returns: the number of apples Billy ate on Wednesday.
    """
    # L1
    apples_monday = 2 # On Monday, he ate 2 apples
    twice_factor = 2 # WK
    apples_tuesday = apples_monday * twice_factor

    # L2
    half_factor = 0.5 # On Friday, he ate half of the amount he ate on Monday
    apples_friday = apples_monday * half_factor

    # L3
    four_times_factor = 4 # On Thursday, he ate four times as many as he ate on Friday
    apples_thursday = four_times_factor * apples_friday

    # L4
    total_apples_known_days = apples_monday + apples_tuesday + apples_thursday + apples_friday

    # L5
    total_apples_week = 20 # Billy ate 20 apples this week
    apples_wednesday = total_apples_week - total_apples_known_days

    # FA
    answer = apples_wednesday
    return answer