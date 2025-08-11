def solve():
    """Index: 506.
    Returns: the average distance Terese runs on each of the days she runs.
    """
    # L1
    monday_miles = 4.2 # Monday, she runs 4.2 miles
    tuesday_miles = 3.8 # Tuesday, 3.8 miles
    wednesday_miles = 3.6 # Wednesday, 3.6 miles
    thursday_miles = 4.4 # Thursday, 4.4 miles
    total_distance = monday_miles + tuesday_miles + thursday_miles + wednesday_miles

    # L2
    num_days = 4 # She runs on 4 days
    average_distance = total_distance / num_days

    # FA
    answer = average_distance
    return answer