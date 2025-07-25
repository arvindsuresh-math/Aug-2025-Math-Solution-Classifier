def solve():
    """Index: 1639.
    Returns: the number of minutes Andy blew up balloons.
    """
    # L1
    total_balloons = 50 # When Andy stopped, there were 50 balloons
    ashley_balloons = 12 # Ashley had already blown up 12 balloons
    andy_balloons = total_balloons - ashley_balloons

    # L2
    balloons_per_increment = 2 # at a rate of 2 every five minutes
    time_increments = andy_balloons / balloons_per_increment

    # L3
    minutes_per_increment = 5 # at a rate of 2 every five minutes
    total_minutes = time_increments * minutes_per_increment

    # FA
    answer = total_minutes
    return answer