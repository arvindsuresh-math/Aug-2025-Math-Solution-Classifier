def solve():
    """Index: 3186.
    Returns: the total number of monsters Chandra needs to lead back to the swamps.
    """
    # L1
    monsters_day1 = 2 # saw 2 monsters
    multiplier_double = 2 # double the amount
    monsters_day2 = monsters_day1 * multiplier_double

    # L2
    monsters_day3 = monsters_day2 * multiplier_double

    # L3
    monsters_day4 = monsters_day3 * multiplier_double

    # L4
    monsters_day5 = monsters_day4 * multiplier_double

    # L5
    total_monsters = monsters_day1 + monsters_day2 + monsters_day3 + monsters_day4 + monsters_day5

    # FA
    answer = total_monsters
    return answer