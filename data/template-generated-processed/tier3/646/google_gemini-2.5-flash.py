from fractions import Fraction

def solve():
    """Index: 646.
    Returns: the total number of people the bus carried on the two trips.
    """
    # L1
    capacity = 200 # A bus has a capacity of 200 people
    first_trip_fraction = Fraction(3, 4) # 3/4 of its capacity
    passengers_first_trip = first_trip_fraction * capacity

    # L2
    return_trip_fraction = Fraction(4, 5) # 4/5 of its capacity
    passengers_return_trip = return_trip_fraction * capacity

    # L3
    total_passengers = passengers_return_trip + passengers_first_trip

    # FA
    answer = total_passengers
    return answer