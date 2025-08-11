def solve():
    """Index: 2516.
    Returns: the percent likelihood that one selected balloon will be red.
    """
    # L1
    initial_red_balloons = 2 # 2 red balloons
    initial_blue_balloons = 4 # 4 blue balloons
    new_balloons_total = 4 # inflates 4 more balloons
    total_balloons = initial_red_balloons + initial_blue_balloons + new_balloons_total

    # L2
    new_red_balloons = 2 # two of each color red and blue
    red_balloons_after_inflation = initial_red_balloons + new_red_balloons
    red_probability_decimal = red_balloons_after_inflation / total_balloons
    red_probability_percent = red_probability_decimal * 100

    # FA
    answer = red_probability_percent
    return answer