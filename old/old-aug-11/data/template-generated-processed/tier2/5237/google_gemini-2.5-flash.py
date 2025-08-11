def solve():
    """Index: 5237.
    Returns: the total miles Wanda walks after 4 weeks.
    """
    # L1
    distance_one_way = 0.5 # .5 miles to school
    trips_per_day = 4 # 4 times a day
    daily_distance = distance_one_way * trips_per_day

    # L2
    days_per_week = 5 # 5 days a week
    weekly_distance = daily_distance * days_per_week

    # L3
    num_weeks = 4 # after 4 weeks
    total_distance = num_weeks * weekly_distance

    # FA
    answer = total_distance
    return answer