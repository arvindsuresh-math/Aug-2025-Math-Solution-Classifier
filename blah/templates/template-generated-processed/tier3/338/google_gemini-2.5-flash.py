def solve():
    """Index: 338.
    Returns: the rate of gasoline consumption in miles per gallon.
    """
    # L1
    supermarket_distance = 5 # supermarket 5 miles away
    supermarket_round_trip = supermarket_distance + supermarket_distance

    # L2
    turn_around_distance = 2 # Two miles into the journey, he turned around
    turn_around_round_trip = turn_around_distance + turn_around_distance

    # L3
    farm_distance = 6 # farm which was 6 miles away
    total_mileage = supermarket_round_trip + turn_around_round_trip + farm_distance

    # L4
    initial_gasoline = 12 # had only 12 gallons of gasoline
    remaining_gasoline = 2 # now has exactly 2 gallons of gasoline left
    gasoline_consumed = initial_gasoline - remaining_gasoline

    # L5
    consumption_rate = total_mileage / gasoline_consumed

    # FA
    answer = consumption_rate
    return answer