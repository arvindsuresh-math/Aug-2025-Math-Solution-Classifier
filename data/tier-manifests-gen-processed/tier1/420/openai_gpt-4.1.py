def solve():
    """Index: 420.
    Returns: the number of minutes Miriam spent cleaning her room.
    """
    # L1
    laundry_minutes = 30 # 30 minutes doing laundry
    bathroom_minutes = 15 # 15 minutes cleaning the bathroom
    homework_minutes = 40 # 40 minutes doing homework
    accounted_minutes = laundry_minutes + bathroom_minutes + homework_minutes

    # L2
    total_hours = 2 # two hours on these tasks
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L3
    room_minutes = total_minutes - accounted_minutes

    # FA
    answer = room_minutes
    return answer