def solve():
    """Index: 998.
    Returns: the time it will take to fill the pool in minutes.
    """
    # L1
    fill_rate_hose = 1.6 # provides water at the rate of 1.6 gallons per minute
    leak_rate_hole = 0.1 # leaks water at a rate of 0.1 gallons per minute
    net_fill_rate = fill_rate_hose - leak_rate_hole

    # L2
    pool_capacity = 60 # pool holds 60 gallons of water
    time_to_fill = pool_capacity / net_fill_rate

    # FA
    answer = time_to_fill
    return answer