from fractions import Fraction

def solve():
    """Index: 646.
    Returns: the total number of people the bus carried on the two trips.
    """
    # L1
    bus_capacity = 200 # a capacity of 200 people
    first_trip_fraction = Fraction(3, 4) # 3/4 of its capacity on its first trip
    first_trip_passengers = first_trip_fraction * bus_capacity

    # L2
    return_trip_fraction = Fraction(4, 5) # 4/5 of its capacity on its return trip
    return_trip_passengers = return_trip_fraction * bus_capacity

    # L3
    total_passengers = return_trip_passengers + first_trip_passengers

    # FA
    answer = total_passengers
    return answer