def solve():
    """Index: 3088.
    Returns: the number of times Keanu has to refill his motorcycle.
    """
    # L1
    destination_miles = 280 # destination is 280 miles away
    round_trip_multiplier = 2 # round trip
    total_round_trip_miles = destination_miles * round_trip_multiplier

    # L2
    miles_per_refill = 40 # consumes 8 liters of gasoline per 40 miles
    num_refills = total_round_trip_miles / miles_per_refill

    # FA
    answer = num_refills
    return answer