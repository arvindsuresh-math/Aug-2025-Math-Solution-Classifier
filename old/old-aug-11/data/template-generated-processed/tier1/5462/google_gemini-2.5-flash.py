def solve():
    """Index: 5462.
    Returns: the total distance in miles between Ann and Glenda.
    """
    # L1
    travel_hours = 3 # for 3 hours
    glenda_speed = 8 # Glenda can skate 8 miles an hour
    glenda_distance = travel_hours * glenda_speed

    # L2
    ann_speed = 6 # Ann can skate 6 miles an hour
    ann_distance = travel_hours * ann_speed

    # L3
    total_distance = ann_distance + glenda_distance

    # FA
    answer = total_distance
    return answer