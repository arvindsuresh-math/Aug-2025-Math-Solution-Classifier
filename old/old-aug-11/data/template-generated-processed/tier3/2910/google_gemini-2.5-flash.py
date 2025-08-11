def solve():
    """Index: 2910.
    Returns: the total number of different passengers stepping on and off a train within an hour.
    """
    # L1
    passengers_leaving = 200 # leaving 200 passengers
    passengers_taking = 320 # taking 320 others
    total_passengers_per_exchange = passengers_leaving + passengers_taking

    # L2
    minutes_per_hour = 60 # WK
    train_frequency_minutes = 5 # a train comes every 5 minutes
    trains_per_hour = minutes_per_hour / train_frequency_minutes

    # L3
    total_different_passengers = trains_per_hour * total_passengers_per_exchange

    # FA
    answer = total_different_passengers
    return answer