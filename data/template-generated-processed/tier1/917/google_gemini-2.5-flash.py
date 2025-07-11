def solve():
    """Index: 917.
    Returns: how much higher Jason will be than Matt.
    """
    # L1
    matt_rate = 6 # 6 feet/minute
    time_climbed = 7 # After 7 minutes
    matt_distance = matt_rate * time_climbed

    # L2
    jason_rate = 12 # 12 feet per minute
    jason_distance = jason_rate * time_climbed

    # L3
    height_difference = jason_distance - matt_distance

    # FA
    answer = height_difference
    return answer