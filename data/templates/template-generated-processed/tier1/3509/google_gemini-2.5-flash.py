def solve():
    """Index: 3509.
    Returns: the total miles Scott will run in a month with 4 weeks.
    """
    # L1
    miles_monday_wednesday_per_day = 3 # 3 miles every Monday through Wednesday
    multiplier_twice_as_far = 2 # twice as far
    miles_thursday_friday_per_day = miles_monday_wednesday_per_day * multiplier_twice_as_far

    # L2
    num_days_mon_wed = 3 # Monday through Wednesday
    total_miles_mon_wed = miles_monday_wednesday_per_day * num_days_mon_wed

    # L3
    num_days_thu_fri = 2 # Thursday and Friday
    total_miles_thu_fri = miles_thursday_friday_per_day * num_days_thu_fri

    # L4
    total_miles_per_week = total_miles_mon_wed + total_miles_thu_fri

    # L5
    num_weeks_in_month = 4 # month with 4 weeks
    total_miles_per_month = total_miles_per_week * num_weeks_in_month

    # FA
    answer = total_miles_per_month
    return answer