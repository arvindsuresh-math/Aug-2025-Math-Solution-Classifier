def solve():
    """Index: 998.
    Returns: the time in minutes to fill the pool.
    """
    # L1
    hose_rate = 1.6 # garden hose provides water at 1.6 gallons per minute
    leak_rate = 0.1 # pool leaks at 0.1 gallons per minute
    net_fill_rate = hose_rate - leak_rate

    # L2
    pool_capacity = 60 # pool holds 60 gallons of water
    time_to_fill = pool_capacity / net_fill_rate

    # FA
    answer = time_to_fill
    return answer