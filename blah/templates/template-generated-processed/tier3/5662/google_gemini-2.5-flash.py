def solve():
    """Index: 5662.
    Returns: the time it will take Karen to paddle up the river.
    """
    # L1
    paddling_speed = 10 # Karen can paddle 10 miles per hour
    current_speed = 4 # The river flows in the opposite direction at 4 miles per hour
    net_speed = paddling_speed - current_speed

    # L2
    river_length = 12 # If the river is 12 miles long
    time_to_paddle = river_length / net_speed

    # FA
    answer = time_to_paddle
    return answer