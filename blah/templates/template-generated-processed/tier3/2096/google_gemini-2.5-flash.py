def solve():
    """Index: 2096.
    Returns: the number of cans of corn Beth bought.
    """
    # L4
    cans_of_peas = 35 # If she bought 35 cans of peas
    more_than_twice_corn = 15 # 15 more cans of peas than twice the number of cans of corn
    twice_corn_cans_value = cans_of_peas - more_than_twice_corn

    # L5
    divisor_for_corn = 2 # twice the number of cans of corn
    cans_of_corn = twice_corn_cans_value / divisor_for_corn

    # FA
    answer = cans_of_corn
    return answer