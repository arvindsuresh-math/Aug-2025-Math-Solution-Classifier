def solve():
    """Index: 1349.
    Returns: the total distance covered by Emerson on his trip.
    """
    # L1
    first_distance = 6 # 6 miles away from his starting point
    additional_distance_1 = 15 # continued for another 15 miles
    distance_after_first_segment = first_distance + additional_distance_1

    # L2
    additional_distance_2 = 18 # covering the remaining 18 miles
    total_distance = additional_distance_2 + distance_after_first_segment

    # FA
    answer = total_distance
    return answer