def solve():
    """Index: 3377.
    Returns: the time in minutes Kyle spends lifting weight.
    """
    # L1
    total_practice_hours = 2 # 2 hours
    half_fraction = 0.5 # Half of the time
    running_weightlifting_hours = half_fraction * total_practice_hours

    # L4
    minutes_per_hour = 60 # WK
    running_weightlifting_minutes = running_weightlifting_hours * minutes_per_hour

    # L5
    total_parts_for_time_division = 3 # WK (from x + 2x = 3x, where 2x is 'twice the time')
    weightlifting_minutes = running_weightlifting_minutes / total_parts_for_time_division

    # FA
    answer = weightlifting_minutes
    return answer