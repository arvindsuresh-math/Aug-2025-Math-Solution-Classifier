def solve():
    """Index: 2561.
    Returns: the number of turtles on Lonely Island.
    """
    # L1
    turtles_happy_island = 60 # Happy Island has 60 turtles
    subtraction_value = 10 # 10 more than
    turtles_after_subtraction = turtles_happy_island - subtraction_value

    # L2
    division_value = 2 # 2 times as many turtles
    turtles_lonely_island = turtles_after_subtraction / division_value

    # FA
    answer = turtles_lonely_island
    return answer