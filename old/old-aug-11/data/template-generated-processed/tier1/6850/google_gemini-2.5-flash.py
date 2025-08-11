def solve():
    """Index: 6850.
    Returns: the total number of guitar strings Dave will need to replace.
    """
    # L1
    strings_per_night = 2 # 2 guitar strings per night
    shows_per_week = 6 # 6 shows a week
    broken_strings_per_week = strings_per_night * shows_per_week

    # L2
    num_weeks = 12 # 12 weeks
    total_strings_needed = broken_strings_per_week * num_weeks

    # FA
    answer = total_strings_needed
    return answer