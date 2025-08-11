def solve():
    """Index: 1150.
    Returns: the total number of miles the driver travels in a week.
    """
    # L1
    hours_first_leg = 3 # 3 hours
    mph_first_leg = 30 # 30 miles per hour
    mph_second_leg = 25 # 25 miles per hour
    hours_second_leg = 4 # 4 hours
    miles_per_day = (hours_first_leg * mph_first_leg) + (mph_second_leg * hours_second_leg)

    # L2
    days_per_week = 6 # Monday to Saturday
    miles_per_week = miles_per_day * days_per_week

    # FA
    answer = miles_per_week
    return answer