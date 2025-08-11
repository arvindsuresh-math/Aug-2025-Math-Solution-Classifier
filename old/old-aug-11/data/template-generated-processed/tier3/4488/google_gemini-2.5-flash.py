def solve():
    """Index: 4488.
    Returns: the time Janet has to wait for her sister.
    """
    # L1
    lake_width = 60 # lake is 60 miles wide
    janet_speed = 30 # going 30 miles per hour
    janet_travel_time = lake_width / janet_speed

    # L2
    sister_speed = 12 # speed of 12 miles per hour
    sister_travel_time = lake_width / sister_speed

    # L3
    wait_time = sister_travel_time - janet_travel_time

    # FA
    answer = wait_time
    return answer