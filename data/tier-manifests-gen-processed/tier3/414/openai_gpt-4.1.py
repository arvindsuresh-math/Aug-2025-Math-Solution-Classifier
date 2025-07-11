def solve():
    """Index: 414.
    Returns: the total amount of caffeine John consumed in grams.
    """
    # L1
    second_drink_ounces = 2 # only 2 ounces
    first_drink_ounces = 12 # 12-ounce drink
    size_ratio = second_drink_ounces / first_drink_ounces

    # L2
    caffeine_multiplier = 3 # 3 times more caffeinated per ounce
    caffeine_ratio = size_ratio * caffeine_multiplier

    # L3
    first_drink_caffeine = 250 # 250 grams of caffeine
    second_drink_caffeine = caffeine_ratio * first_drink_caffeine

    # L4
    total_drink_caffeine = second_drink_caffeine + first_drink_caffeine

    # L5
    caffeine_pill_multiplier = 2 # caffeine pill that has as much caffeine as his 2 drinks combined
    total_caffeine = total_drink_caffeine * caffeine_pill_multiplier

    # FA
    answer = total_caffeine
    return answer