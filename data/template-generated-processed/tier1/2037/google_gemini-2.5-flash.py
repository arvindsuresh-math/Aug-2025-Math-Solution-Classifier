def solve():
    """Index: 2037.
    Returns: the total time in seconds for the three to run the 600-meter relay race.
    """
    # L1
    rhonda_time_200m = 24 # Rhonda can run 200 meters in 24 seconds
    sally_longer_than_rhonda = 2 # Sally takes two seconds longer
    sally_time_200m = rhonda_time_200m + sally_longer_than_rhonda

    # L2
    diane_faster_than_rhonda = 3 # Diane can run 200 meters three seconds faster than Rhonda
    diane_time_200m = rhonda_time_200m - diane_faster_than_rhonda

    # L3
    total_relay_time = rhonda_time_200m + sally_time_200m + diane_time_200m

    # FA
    answer = total_relay_time
    return answer