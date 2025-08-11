def solve():
    """Index: 6418.
    Returns: the remaining miles Macy needs to run to meet her goal.
    """
    # L1
    miles_per_day = 3 # runs 3 miles per day
    num_days = 6 # after 6 days
    miles_run_in_6_days = miles_per_day * num_days

    # L2
    weekly_goal = 24 # goal of running a total of 24 miles per week
    miles_left = weekly_goal - miles_run_in_6_days

    # FA
    answer = miles_left
    return answer