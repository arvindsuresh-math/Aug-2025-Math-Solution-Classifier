def solve():
    """Index: 553.
    Returns: the total number of containers of milk Emma buys.
    """
    # L1
    school_days_per_week = 5 # WK
    containers_per_school_day = 2 # 2 containers of milk every school day
    containers_per_week = school_days_per_week * containers_per_school_day

    # L2
    num_weeks = 3 # 3 weeks
    total_containers = num_weeks * containers_per_week

    # FA
    answer = total_containers
    return answer