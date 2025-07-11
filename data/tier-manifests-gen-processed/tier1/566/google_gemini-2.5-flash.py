def solve():
    """Index: 566.
    Returns: the speed at which the red car can travel in miles per hour.
    """
    # L1
    blue_car_speed = 80 # blue one can travel at a speed of 80 miles per hour
    multiplier_green_from_blue = 8 # green one can travel at 8 times the speed of the blue one
    green_car_speed = multiplier_green_from_blue * blue_car_speed

    # L2
    multiplier_red_from_green = 2 # red one can travel at twice the speed of the green one
    red_car_speed = multiplier_red_from_green * green_car_speed

    # FA
    answer = red_car_speed
    return answer