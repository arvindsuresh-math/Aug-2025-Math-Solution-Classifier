def solve():
    """Index: 2137.
    Returns: the number of tomatoes that grew in Grandpa's absence.
    """
    # L2
    initial_tomatoes_count = 36 # 36 small tomatoes
    times_multiplier = 100 # 100 times more tomatoes
    total_tomatoes_after_vacation = times_multiplier * initial_tomatoes_count

    # L3
    tomatoes_grown_in_absence = total_tomatoes_after_vacation - initial_tomatoes_count

    # FA
    answer = tomatoes_grown_in_absence
    return answer