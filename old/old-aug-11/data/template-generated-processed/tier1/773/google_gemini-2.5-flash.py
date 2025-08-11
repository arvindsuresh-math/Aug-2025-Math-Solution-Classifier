def solve():
    """Index: 773.
    Returns: the number of miles they still need to travel.
    """
    # L1
    amoli_speed = 42 # 42 miles an hour
    amoli_time = 3 # 3 hours
    amoli_distance = amoli_speed * amoli_time

    # L2
    anayet_speed = 61 # 61 miles an hour
    anayet_time = 2 # 2 hours
    anayet_distance = anayet_speed * anayet_time

    # L3
    total_distance_driven = amoli_distance + anayet_distance

    # L4
    total_miles_to_travel = 369 # travel 369 miles together
    remaining_miles = total_miles_to_travel - total_distance_driven

    # FA
    answer = remaining_miles
    return answer