def solve():
    """Index: 338.
    Returns: the rate in miles per gallon Bobby's truck has been consuming gasoline.
    """
    # L1
    supermarket_distance = 5 # drives to a supermarket 5 miles away
    supermarket_trip = supermarket_distance + supermarket_distance

    # L2
    partial_farm_leg = 2 # Two miles into the journey
    partial_farm_trip = partial_farm_leg + partial_farm_leg

    # L3
    farm_distance = 6 # which was 6 miles away
    total_mileage = supermarket_trip + partial_farm_trip + farm_distance

    # L4
    initial_gasoline = 12 # had only 12 gallons of gasoline
    gasoline_left = 2 # now has exactly 2 gallons of gasoline left
    gasoline_used = initial_gasoline - gasoline_left

    # L5
    rate = total_mileage / gasoline_used

    # FA
    answer = rate
    return answer