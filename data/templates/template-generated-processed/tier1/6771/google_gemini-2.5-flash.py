def solve():
    """Index: 6771.
    Returns: the total number of pull-ups Mike does a week.
    """
    # L1
    entries_per_day = 5 # goes in there 5 times a day
    pullups_per_entry = 2 # does 2 pull-ups
    pullups_per_day = entries_per_day * pullups_per_entry

    # L2
    days_per_week = 7 # WK
    pullups_per_week = pullups_per_day * days_per_week

    # FA
    answer = pullups_per_week
    return answer