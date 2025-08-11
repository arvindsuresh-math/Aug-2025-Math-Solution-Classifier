def solve():
    """Index: 420.
    Returns: the time spent cleaning her room in minutes.
    """
    # L1
    laundry_minutes = 30 # 30 minutes doing laundry
    bathroom_minutes = 15 # 15 minutes cleaning the bathroom
    homework_minutes = 40 # 40 minutes doing homework
    total_accounted_minutes = laundry_minutes + bathroom_minutes + homework_minutes

    # L2
    total_hours = 2 # two hours on these tasks
    minutes_per_hour = 60 # WK
    total_minutes_spent = total_hours * minutes_per_hour

    # L3
    room_cleaning_minutes = total_minutes_spent - total_accounted_minutes

    # FA
    answer = room_cleaning_minutes
    return answer