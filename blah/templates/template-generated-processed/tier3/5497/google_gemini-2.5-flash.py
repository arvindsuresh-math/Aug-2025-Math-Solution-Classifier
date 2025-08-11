from fractions import Fraction

def solve():
    """Index: 5497.
    Returns: the total time in minutes to fill the pool.
    """
    # L1
    pool_capacity = 84 # pool holds 84 gallons of water
    bucket_capacity = 2 # 2 gallon bucket
    number_of_trips = pool_capacity / bucket_capacity

    # L2
    time_per_trip_seconds = 20 # 20 seconds to fill the bucket from the tap and carry it to the pool
    total_time_seconds = number_of_trips * time_per_trip_seconds

    # L3
    minutes_per_second_fraction = Fraction(1, 60) # WK
    total_time_minutes = total_time_seconds * minutes_per_second_fraction

    # FA
    answer = total_time_minutes
    return answer