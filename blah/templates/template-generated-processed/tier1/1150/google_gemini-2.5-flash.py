def solve():
    """Index: 1150.
    Returns: the total miles the driver travels in a week.
    """
    # L1
    first_duration_hours = 3 # 3 hours
    first_speed_mph = 30 # 30 miles per hour
    second_speed_mph = 25 # 25 miles per hour
    second_duration_hours = 4 # 4 hours
    miles_per_day = (first_duration_hours * first_speed_mph) + (second_speed_mph * second_duration_hours)

    # L2
    delivery_days_per_week = 6 # from Monday to Saturday
    total_miles_per_week = miles_per_day * delivery_days_per_week

    # FA
    answer = total_miles_per_week
    return answer