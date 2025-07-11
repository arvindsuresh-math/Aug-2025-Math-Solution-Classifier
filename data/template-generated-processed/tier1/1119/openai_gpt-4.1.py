def solve():
    """Index: 1119.
    Returns: the total number of minutes Jill spent talking to her boyfriend that week.
    """
    # L1
    day1_minutes = 5 # spends 5 minutes on the phone the first day
    double = 2 # twice as much time
    day2_minutes = day1_minutes * double

    # L2
    day3_minutes = day2_minutes * double

    # L3
    day4_minutes = day3_minutes * double

    # L4
    day5_minutes = day4_minutes * double

    # L5
    total_minutes = day1_minutes + day2_minutes + day3_minutes + day4_minutes + day5_minutes

    # FA
    answer = total_minutes
    return answer