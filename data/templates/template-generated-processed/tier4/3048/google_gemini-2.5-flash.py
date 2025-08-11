def solve():
    """Index: 3048.
    Returns: the number of substitute teachers left after lunch.
    """
    # L1
    initial_teachers = 60 # 60 substitute teachers show up at 7 AM
    half_quit_divisor = 2 # 50% of substitute teachers walk out after 1 hour of teaching
    teachers_after_hour = initial_teachers / half_quit_divisor

    # L2
    remainder_quit_percent_num = 30 # 30% of the remainder quit before lunch
    percent_factor = 0.01 # WK
    teachers_quit_before_lunch = teachers_after_hour * remainder_quit_percent_num * percent_factor

    # L3
    teachers_after_lunch = teachers_after_hour - teachers_quit_before_lunch

    # FA
    answer = teachers_after_lunch
    return answer