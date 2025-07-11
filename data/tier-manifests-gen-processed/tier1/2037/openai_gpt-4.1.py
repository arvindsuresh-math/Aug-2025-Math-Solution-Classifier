def solve():
    """Index: 2037.
    Returns: the total time in seconds for Rhonda, Sally, and Diane to run the 600-meter relay race.
    """
    # L1
    rhonda_time = 24 # Rhonda can run 200 meters in 24 seconds
    sally_extra = 2 # Sally takes two seconds longer
    sally_time = rhonda_time + sally_extra

    # L2
    diane_faster = 3 # Diane can run 200 meters three seconds faster
    diane_time = rhonda_time - diane_faster

    # L3
    total_time = rhonda_time + sally_time + diane_time

    # FA
    answer = total_time
    return answer