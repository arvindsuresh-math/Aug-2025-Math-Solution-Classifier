def solve():
    """Index: 1863.
    Returns: the time it will take to get from Edmonton to Calgary.
    """
    # L1
    distance_edmonton_red_deer = 220 # Edmonton is 220 kilometers north of Red Deer
    distance_calgary_red_deer = 110 # Calgary is 110 kilometers south of Red Deer
    total_distance = distance_edmonton_red_deer + distance_calgary_red_deer

    # L2
    travel_speed = 110 # If you travel at 110 kilometers per hour
    travel_time = total_distance / travel_speed

    # FA
    answer = travel_time
    return answer