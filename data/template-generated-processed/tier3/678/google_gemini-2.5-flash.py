def solve():
    """Index: 678.
    Returns: the time it takes for the border collie to catch up to the ball.
    """
    # L1
    ball_speed = 20 # 20 feet/second
    flight_time = 8 # 8 seconds
    total_distance = ball_speed * flight_time

    # L2
    dog_speed = 5 # 5 feet/second
    time_to_catch_up = total_distance / dog_speed

    # FA
    answer = time_to_catch_up
    return answer