def solve():
    """Index: 5407.
    Returns: the total number of minutes Jill studied over 3 days.
    """
    # L1
    hours_day1 = 2 # study one day for 2 hours
    double_factor = 2 # doubles this amount
    hours_day2 = hours_day1 * double_factor

    # L2
    less_than_previous_day = 1 # one hour less than the previous day
    hours_day3 = hours_day2 - less_than_previous_day

    # L3
    total_hours = hours_day1 + hours_day2 + hours_day3

    # L4
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # FA
    answer = total_minutes
    return answer