def solve():
    """Index: 5197.
    Returns: the total number of times they rode their bikes.
    """
    # L1
    billy_rides = 17 # Billy rode his bike 17 times
    john_multiplier = 2 # twice as many times
    john_rides = billy_rides * john_multiplier

    # L2
    mother_more_than_john = 10 # 10 times more than John
    mother_rides = john_rides + mother_more_than_john

    # L3
    total_rides = mother_rides + john_rides + billy_rides

    # FA
    answer = total_rides
    return answer