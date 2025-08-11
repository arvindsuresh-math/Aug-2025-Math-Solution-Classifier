def solve():
    """Index: 5093.
    Returns: the number of times Maurice had been horseback riding before visiting Matt.
    """
    # L1
    matt_additional_rides = 16 # Meanwhile, besides the times that Matt accompanied Maurice, he rode an additional 16 times.
    maurice_rides_with_matt = 8 # he rode another 8 times.
    total_matt_rides = matt_additional_rides + maurice_rides_with_matt

    # L2
    times_factor = 3 # three times the number of times Maurice had ridden before his visit
    maurice_rides_before_visit = total_matt_rides / times_factor

    # FA
    answer = maurice_rides_before_visit
    return answer