def solve():
    """Index: 566.
    Returns: the speed in mph at which the red car can travel.
    """
    # L1
    blue_speed = 80 # blue one can travel at a speed of 80 miles per hour
    green_to_blue_ratio = 8 # green one can travel at 8 times the speed of the blue one
    green_speed = green_to_blue_ratio * blue_speed

    # L2
    red_to_green_ratio = 2 # red one can travel at twice the speed of the green one
    red_speed = red_to_green_ratio * green_speed

    # FA
    answer = red_speed
    return answer