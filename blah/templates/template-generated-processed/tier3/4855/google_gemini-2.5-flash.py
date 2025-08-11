def solve():
    """Index: 4855.
    Returns: the distance Danny drives between the second friend's house and work.
    """
    # L1
    distance_to_first_friend = 8 # 8 miles to the first friend's house
    half_divisor = 2 # half that distance
    distance_to_second_friend = distance_to_first_friend / half_divisor

    # L2
    total_distance_so_far = distance_to_second_friend + distance_to_first_friend

    # L3
    triple_multiplier = 3 # 3 times the total distance driven so far
    distance_second_friend_to_work = total_distance_so_far * triple_multiplier

    # FA
    answer = distance_second_friend_to_work
    return answer