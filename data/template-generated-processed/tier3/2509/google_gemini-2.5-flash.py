def solve():
    """Index: 2509.
    Returns: the total hours Sam spends studying the three subjects.
    """
    # L1
    science_minutes = 60 # sixty minutes studying Science
    math_minutes = 80 # eighty minutes in Math
    literature_minutes = 40 # forty minutes in Literature
    total_minutes = science_minutes + math_minutes + literature_minutes

    # L2
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer