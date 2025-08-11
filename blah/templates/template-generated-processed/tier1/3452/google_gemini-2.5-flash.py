def solve():
    """Index: 3452.
    Returns: the remaining screen time in minutes for the evening.
    """
    # L1
    recommended_hours = 2 # 2 hours of screen time
    minutes_per_hour = 60 # WK
    total_allowed_minutes = recommended_hours * minutes_per_hour

    # L2
    used_minutes_morning = 45 # used his gadget for 45 minutes in the morning
    remaining_minutes_evening = total_allowed_minutes - used_minutes_morning

    # FA
    answer = remaining_minutes_evening
    return answer