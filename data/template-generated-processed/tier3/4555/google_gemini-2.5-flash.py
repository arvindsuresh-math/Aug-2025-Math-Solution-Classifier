def solve():
    """Index: 4555.
    Returns: the number of weeks the chocolate eggs will last.
    """
    # L1
    eggs_per_day = 2 # two each day after school
    school_days_per_week = 5 # WK
    eggs_per_week = eggs_per_day * school_days_per_week

    # L2
    total_eggs = 40 # 40 chocolate eggs
    weeks_last = total_eggs / eggs_per_week

    # FA
    answer = weeks_last
    return answer