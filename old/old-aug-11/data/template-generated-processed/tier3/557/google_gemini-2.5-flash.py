def solve():
    """Index: 557.
    Returns: the number of tomatoes left.
    """
    # L1
    num_plants = 18 # 18 plants
    tomatoes_per_plant = 7 # 7 tomatoes each
    total_tomatoes_harvested = num_plants * tomatoes_per_plant

    # L2
    dried_divisor = 2 # dries half the tomatoes
    tomatoes_left_undried = total_tomatoes_harvested / dried_divisor

    # L3
    sauce_divisor = 3 # turns a third of the remainder
    tomatoes_for_sauce = tomatoes_left_undried / sauce_divisor

    # L4
    remaining_tomatoes = tomatoes_left_undried - tomatoes_for_sauce

    # FA
    answer = remaining_tomatoes
    return answer