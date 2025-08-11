def solve():
    """Index: 5257.
    Returns: the number of sheets of paper Evelyn uses per day at work.
    """
    # L1
    days_in_a_week = 7 # WK
    days_off_per_week = 2 # takes Monday and Friday off from work
    work_days_per_week = days_in_a_week - days_off_per_week

    # L2
    total_sheets_per_pad = 60 # A pad of paper comes with 60 sheets
    sheets_per_day = total_sheets_per_pad / work_days_per_week

    # FA
    answer = sheets_per_day
    return answer