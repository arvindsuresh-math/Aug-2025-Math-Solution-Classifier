def solve():
    """Index: 5762.
    Returns: the total number of hours required to complete all lice checks.
    """
    # L1
    kindergarteners = 26 # 26 Kindergarteners
    first_graders = 19 # 19 first graders
    second_graders = 20 # 20 second graders
    third_graders = 25 # 25 third graders
    total_students = kindergarteners + first_graders + second_graders + third_graders

    # L2
    minutes_per_check = 2 # each check takes 2 minutes
    total_minutes = total_students * minutes_per_check

    # L3
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer