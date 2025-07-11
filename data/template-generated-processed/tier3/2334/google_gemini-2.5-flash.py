def solve():
    """Index: 2334.
    Returns: the number of fish in the third fish tank.
    """
    # L1
    goldfish_first_tank = 7 # 7 goldfish
    beta_fish_first_tank = 8 # 8 beta fish
    fish_first_tank = goldfish_first_tank + beta_fish_first_tank

    # L2
    multiplier_second_tank = 2 # twice as many fish
    fish_second_tank = fish_first_tank * multiplier_second_tank

    # L3
    divisor_third_tank = 3 # a third of the number of fish
    fish_third_tank = fish_second_tank / divisor_third_tank

    # FA
    answer = fish_third_tank
    return answer