def solve():
    """Index: 1868.
    Returns: the number of feet left for Max to catch up to Alex.
    """
    # L1
    even_distance = 200 # even with each other for 200 feet
    alex_ahead_1 = 300 # Alex gets ahead by 300 feet
    max_ahead = 170 # Max gets ahead by 170 feet
    alex_ahead_2 = 440 # Alex gets ahead by 440 feet
    distance_covered = even_distance + alex_ahead_1 + max_ahead + alex_ahead_2

    # L2
    total_road_length = 5000 # the road they're running on is 5000 feet long
    feet_left = total_road_length - distance_covered

    # FA
    answer = feet_left
    return answer