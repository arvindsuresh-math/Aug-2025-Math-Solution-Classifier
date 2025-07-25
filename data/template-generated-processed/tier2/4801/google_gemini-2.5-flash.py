def solve():
    """Index: 4801.
    Returns: the total miles Tom runs in a week.
    """
    # L1
    hours_per_day = 1.5 # 1.5 hours each day
    speed = 8 # speed of 8 mph
    miles_per_day = hours_per_day * speed

    # L2
    days_per_week = 5 # 5 days a week
    total_miles_per_week = days_per_week * miles_per_day

    # FA
    answer = total_miles_per_week
    return answer