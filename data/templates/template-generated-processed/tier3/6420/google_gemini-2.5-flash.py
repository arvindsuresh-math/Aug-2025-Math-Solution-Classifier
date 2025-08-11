def solve():
    """Index: 6420.
    Returns: the total distance Rich walked.
    """
    # L1
    initial_walk_to_sidewalk = 20 # 20 feet from his house to the sidewalk
    walk_down_sidewalk = 200 # 200 feet down the sidewalk
    distance_to_end_of_road = initial_walk_to_sidewalk + walk_down_sidewalk

    # L2
    double_factor = 2 # double his total distance so far
    distance_to_next_intersection = distance_to_end_of_road * double_factor

    # L3
    total_distance_so_far_after_intersection = distance_to_end_of_road + distance_to_next_intersection

    # L4
    half_factor = 2 # half the total distance
    distance_to_end_of_route = total_distance_so_far_after_intersection / half_factor

    # L5
    total_distance_one_way = total_distance_so_far_after_intersection + distance_to_end_of_route

    # L6
    return_factor = 2 # walking the same path all the way back home
    total_walked_distance = total_distance_one_way * return_factor

    # FA
    answer = total_walked_distance
    return answer