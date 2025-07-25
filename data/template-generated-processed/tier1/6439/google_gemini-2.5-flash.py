def solve():
    """Index: 6439.
    Returns: the total number of push-ups Geli will do in her first week.
    """
    # L1
    initial_pushups = 10 # started doing 10 push-ups
    day1_pushups = initial_pushups

    # L2
    pushup_increase = 5 # add 5 more push-ups each day
    day2_pushups = day1_pushups + pushup_increase

    # L3
    day3_pushups = day2_pushups + pushup_increase

    # L4
    total_pushups = day1_pushups + day2_pushups + day3_pushups

    # FA
    answer = total_pushups
    return answer