def solve():
    """Index: 158.
    Returns: the number of miles Jerome will ride on the 13th day to finish his goal.
    """
    # L1
    miles_per_day = 12 # ride 12 miles
    num_days = 12 # for 12 days
    miles_in_12_days = miles_per_day * num_days

    # L2
    total_goal = 150 # 150-mile bicycle trip
    miles_on_13th_day = total_goal - miles_in_12_days

    # FA
    answer = miles_on_13th_day
    return answer