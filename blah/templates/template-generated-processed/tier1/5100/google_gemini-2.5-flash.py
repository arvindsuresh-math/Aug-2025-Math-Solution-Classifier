def solve():
    """Index: 5100.
    Returns: the initial number of white lights Malcolm had.
    """
    # L1
    red_lights = 12 # 12 red lights
    blue_light_multiplier = 3 # 3 times as many blue lights
    blue_lights = red_lights * blue_light_multiplier

    # L2
    green_lights = 6 # 6 green lights
    total_bought_colored_lights = red_lights + blue_lights + green_lights

    # L3
    lights_left_to_buy = 5 # 5 colored lights left to buy
    initial_white_lights = total_bought_colored_lights + lights_left_to_buy

    # FA
    answer = initial_white_lights
    return answer