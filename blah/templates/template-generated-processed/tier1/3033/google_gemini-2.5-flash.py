def solve():
    """Index: 3033.
    Returns: the distance the birdhouse had flown in feet.
    """
    # L1
    car_transported_distance = 200 # transported it 200 feet
    lawn_chair_multiplier = 2 # blown twice as far
    lawn_chair_distance = lawn_chair_multiplier * car_transported_distance

    # L2
    birdhouse_multiplier = 3 # three times farther
    birdhouse_distance = birdhouse_multiplier * lawn_chair_distance

    # FA
    answer = birdhouse_distance
    return answer