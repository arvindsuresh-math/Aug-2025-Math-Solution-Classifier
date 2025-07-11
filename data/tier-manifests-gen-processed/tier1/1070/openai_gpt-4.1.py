def solve():
    """Index: 1070.
    Returns: the number of eggs Jason will consume in two weeks.
    """
    # L1
    days_per_week = 7 # WK
    num_weeks = 2 # two weeks
    total_days = days_per_week * num_weeks

    # L2
    eggs_per_day = 3 # three eggs per day
    total_eggs = eggs_per_day * total_days

    # FA
    answer = total_eggs
    return answer