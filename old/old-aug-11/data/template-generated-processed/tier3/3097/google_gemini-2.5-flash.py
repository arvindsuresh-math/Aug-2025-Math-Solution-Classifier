def solve():
    """Index: 3097.
    Returns: the number of hours Yara will be ahead of Theon.
    """
    # L1
    destination_distance = 90 # destination is 90 nautical miles away
    theon_speed = 15 # Theon's ship can move 15 nautical miles per hour
    theon_eta = destination_distance / theon_speed

    # L2
    yara_speed = 30 # Yara's ship can move 30 nautical miles per hour
    yara_eta = destination_distance / yara_speed

    # L3
    time_difference = theon_eta - yara_eta

    # FA
    answer = time_difference
    return answer