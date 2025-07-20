def solve():
    """Index: 4950.
    Returns: Nero's speed in MPH.
    """
    # L1
    jerome_speed = 4 # Jerome runs at 4 MPH
    jerome_time = 6 # It takes Jerome 6 hours
    trail_distance = jerome_speed * jerome_time

    # L2
    nero_time = 3 # it takes Nero 3 hours
    nero_speed = trail_distance / nero_time

    # FA
    answer = nero_speed
    return answer