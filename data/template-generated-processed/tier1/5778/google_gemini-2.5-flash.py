def solve():
    """Index: 5778.
    Returns: the total hours Carl will drive in two weeks.
    """
    # L1
    additional_hours_per_week = 6 # 6 more hours every week
    num_weeks = 2 # two weeks
    total_additional_hours = num_weeks * additional_hours_per_week

    # L2
    hours_per_day_initial = 2 # 2 hours every day
    days_in_two_weeks = 14 # WK
    regular_driving_hours = days_in_two_weeks * hours_per_day_initial

    # L3
    total_driving_hours = regular_driving_hours + total_additional_hours

    # FA
    answer = total_driving_hours
    return answer