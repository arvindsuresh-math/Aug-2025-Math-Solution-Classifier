def solve():
    """Index: 5499.
    Returns: how much farther Grayson travels compared to Rudy.
    """
    # L1
    grayson_initial_time = 1 # 1 hour
    grayson_initial_speed = 25 # 25 mph
    grayson_initial_distance = grayson_initial_time * grayson_initial_speed

    # L2
    grayson_second_time = 0.5 # 0.5 hours
    grayson_second_speed = 20 # 20 mph
    grayson_second_distance = grayson_second_time * grayson_second_speed

    # L3
    grayson_total_distance = grayson_initial_distance + grayson_second_distance

    # L4
    rudy_time = 3 # 3 hours
    rudy_speed = 10 # 10 mph
    rudy_total_distance = rudy_time * rudy_speed

    # L5
    distance_difference = grayson_total_distance - rudy_total_distance

    # FA
    answer = distance_difference
    return answer