def solve():
    """Index: 4279.
    Returns: the time Bill spent working on the project.
    """
    # L1
    hours_per_day = 24 # WK
    project_days = 4 # 4 days
    total_project_hours = hours_per_day * project_days

    # L2
    num_naps = 6 # 6 seven-hour naps
    nap_duration_hours = 7 # seven-hour naps
    total_nap_hours = num_naps * nap_duration_hours

    # L3
    working_hours = total_project_hours - total_nap_hours

    # FA
    answer = working_hours
    return answer