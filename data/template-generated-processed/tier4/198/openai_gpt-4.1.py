def solve():
    """Index: 198.
    Returns: the number of minutes Rosie should run on Friday to reach her weekly goal.
    """
    # L1
    speed_mph = 6 # Rosie runs 6 miles per hour
    mon_run_hours = 1 # 1 hour on Monday
    wed_run_hours = 1 # 1 hour on Wednesday
    mon_miles = speed_mph * mon_run_hours
    wed_miles = speed_mph * wed_run_hours

    # L2
    tue_run_minutes = 30 # 30 minutes on Tuesday
    minutes_per_hour = 60 # WK
    tue_miles = speed_mph * (tue_run_minutes / minutes_per_hour)

    # L3
    thu_run_minutes = 20 # 20 minutes on Thursday
    thu_miles = speed_mph * (thu_run_minutes / minutes_per_hour)

    # L4
    total_miles_so_far = mon_miles + tue_miles + wed_miles + thu_miles

    # L5
    weekly_goal = 20 # wants to run 20 miles for the week
    miles_needed_friday = weekly_goal - total_miles_so_far

    # L6
    friday_run_hours = miles_needed_friday / speed_mph
    friday_run_minutes = friday_run_hours * minutes_per_hour

    # FA
    answer = friday_run_minutes
    return answer