def solve():
    """Index: 773.
    Returns: the number of miles Amoli and Anayet still need to travel.
    """
    # L1
    amoli_speed = 42 # Amoli drove 42 miles an hour
    amoli_time = 3 # for 3 hours
    amoli_distance = amoli_speed * amoli_time

    # L2
    anayet_speed = 61 # Anayet drove at 61 miles an hour
    anayet_time = 2 # for 2 hours
    anayet_distance = anayet_speed * anayet_time

    # L3
    total_distance_covered = amoli_distance + anayet_distance

    # L4
    total_distance = 369 # must travel 369 miles together
    miles_remaining = total_distance - total_distance_covered

    # FA
    answer = miles_remaining
    return answer