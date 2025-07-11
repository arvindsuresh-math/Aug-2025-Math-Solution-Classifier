def solve():
    """Index: 1349.
    Returns: the total distance covered by Emerson on his trip.
    """
    # L1
    first_leg = 6 # was 6 miles away from his starting point
    second_leg = 15 # continued for another 15 miles
    after_second_leg = first_leg + second_leg

    # L2
    third_leg = 18 # covering the remaining 18 miles
    total_distance = third_leg + after_second_leg

    # FA
    answer = total_distance
    return answer