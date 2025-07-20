def solve():
    """Index: 4405.
    Returns: the number of feet between the first and second signs.
    """
    # L1
    total_ride_distance = 1000 # rode a total of 1000 feet
    distance_to_first_sign = 350 # stop sign that was 350 feet away from his house
    distance_after_first_sign = total_ride_distance - distance_to_first_sign

    # L2
    distance_after_second_sign = 275 # After passing the second sign he road an additional 275 feet
    distance_between_signs = distance_after_first_sign - distance_after_second_sign

    # FA
    answer = distance_between_signs
    return answer