def solve():
    """Index: 553.
    Returns: the number of containers of milk Emma buys in 3 weeks.
    """
    # L1
    school_days_per_week = 5 # does not go to school on the weekends
    containers_per_day = 2 # buys 2 containers of milk every school day
    containers_per_week = school_days_per_week * containers_per_day

    # L2
    num_weeks = 3 # in 3 weeks
    total_containers = num_weeks * containers_per_week

    # FA
    answer = total_containers
    return answer