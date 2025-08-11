def solve():
    """Index: 644.
    Returns: the total number of people the bus system carries for 13 weeks.
    """
    # L1
    num_weeks = 13 # 13 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L2
    people_per_day = 1200000 # 1,200,000 people each day
    total_people_carried = people_per_day * total_days

    # FA
    answer = total_people_carried
    return answer