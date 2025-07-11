def solve():
    """Index: 1849.
    Returns: the total number of miles Jennifer travels to both museums and back.
    """
    # L1
    first_museum_distance = 5 # 5 miles away from her home
    round_trip_first = first_museum_distance + first_museum_distance

    # L2
    second_museum_distance = 15 # 15 miles away
    round_trip_second = second_museum_distance + second_museum_distance

    # L3
    total_miles = round_trip_first + round_trip_second

    # FA
    answer = total_miles
    return answer