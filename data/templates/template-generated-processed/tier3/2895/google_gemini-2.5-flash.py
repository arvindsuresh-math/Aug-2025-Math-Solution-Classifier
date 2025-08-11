def solve():
    """Index: 2895.
    Returns: the total hours it took Joan to get to her family.
    """
    # L1
    distance = 480 # 480 miles away
    speed = 60 # 60 mph
    driving_time_hours = distance / speed

    # L2
    lunch_break_duration = 30 # 30 minutes
    first_bathroom_break_duration = 15 # 15 minutes each
    second_bathroom_break_duration = 15 # 15 minutes each
    total_break_minutes = lunch_break_duration + first_bathroom_break_duration + second_bathroom_break_duration

    # L3
    minutes_per_hour = 60 # WK
    total_break_hours = total_break_minutes / minutes_per_hour

    # L4
    total_travel_time_hours = driving_time_hours + total_break_hours

    # FA
    answer = total_travel_time_hours
    return answer