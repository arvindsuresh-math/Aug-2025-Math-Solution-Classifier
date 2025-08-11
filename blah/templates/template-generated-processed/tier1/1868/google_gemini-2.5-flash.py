def solve():
    """Index: 1868.
    Returns: the number of feet left for Max to catch up to Alex.
    """
    # L1
    initial_even_distance = 200 # 200 feet
    alex_ahead_1 = 300 # Alex gets ahead of Max by 300 feet
    max_ahead_1 = 170 # Max gets ahead of Alex by 170 feet
    alex_ahead_2 = 440 # Alex gets ahead of Max by 440 feet
    total_distance_covered = initial_even_distance + alex_ahead_1 + max_ahead_1 + alex_ahead_2

    # L2
    total_road_length = 5000 # road they're running on is 5000 feet long
    remaining_distance = total_road_length - total_distance_covered

    # FA
    answer = remaining_distance
    return answer