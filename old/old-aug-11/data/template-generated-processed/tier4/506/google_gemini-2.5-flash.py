def solve():
    """Index: 506.
    Returns: the average distance Terese runs on each of the days she runs.
    """
    # L1
    monday_distance = 4.2 # On Monday, she runs 4.2 miles
    tuesday_distance = 3.8 # Tuesday, 3.8 miles
    wednesday_distance = 3.6 # Wednesday, 3.6 miles
    thursday_distance = 4.4 # on Thursday, 4.4 miles
    total_distance = monday_distance + tuesday_distance + thursday_distance + wednesday_distance

    # L2
    num_days_run = 4 # Monday, Tuesday, Wednesday, and Thursday
    average_distance = total_distance / num_days_run

    # FA
    answer = average_distance
    return answer