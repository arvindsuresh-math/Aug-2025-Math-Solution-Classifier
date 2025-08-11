def solve():
    """Index: 1843.
    Returns: the total gallons Martha's car requires for the trip.
    """
    # L1
    darlene_mpg = 20 # Darlene's car gets 20 miles/gallon
    half_divisor = 2 # half as many miles per gallon
    martha_mpg = darlene_mpg / half_divisor

    # L2
    trip_distance = 300 # a 300-mile trip
    total_gallons_required = trip_distance / martha_mpg

    # FA
    answer = total_gallons_required
    return answer