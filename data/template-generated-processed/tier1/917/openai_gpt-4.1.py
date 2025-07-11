def solve():
    """Index: 917.
    Returns: how much higher Jason will be than Matt after 7 minutes.
    """
    # L1
    matt_speed = 6 # Matt can climb 6 feet/minute
    minutes = 7 # After 7 minutes
    matt_distance = matt_speed * minutes

    # L2
    jason_speed = 12 # Jason can climb 12 feet per minute
    jason_distance = jason_speed * minutes

    # L3
    difference = jason_distance - matt_distance

    # FA
    answer = difference
    return answer