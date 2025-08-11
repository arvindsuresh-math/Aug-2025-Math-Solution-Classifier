def solve():
    """Index: 557.
    Returns: the number of tomatoes left after drying and making sauce.
    """
    # L1
    num_plants = 18 # 18 plants
    tomatoes_per_plant = 7 # 7 tomatoes each
    total_tomatoes = num_plants * tomatoes_per_plant

    # L2
    dried_divisor = 2 # dries half the tomatoes
    undried_tomatoes = total_tomatoes / dried_divisor

    # L3
    sauce_divisor = 3 # turns a third of the remainder into marinara sauce
    tomatoes_for_sauce = undried_tomatoes / sauce_divisor

    # L4
    tomatoes_left = undried_tomatoes - tomatoes_for_sauce

    # FA
    answer = tomatoes_left
    return answer