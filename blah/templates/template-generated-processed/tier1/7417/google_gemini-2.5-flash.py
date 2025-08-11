def solve():
    """Index: 7417.
    Returns: the total number of filled water balloons Max and Zach have.
    """
    # L1
    max_fill_time = 30 # for 30 minutes
    max_fill_rate = 2 # 2 water balloons every minute
    max_balloons = max_fill_time * max_fill_rate

    # L2
    zach_fill_time = 40 # for 40 minutes
    zach_fill_rate = 3 # 3 water balloons every minute
    zach_balloons = zach_fill_time * zach_fill_rate

    # L3
    popped_balloons = 10 # 10 of the water balloons pop
    total_remaining_balloons = max_balloons + zach_balloons - popped_balloons

    # FA
    answer = total_remaining_balloons
    return answer