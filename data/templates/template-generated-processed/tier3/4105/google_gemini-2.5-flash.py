def solve():
    """Index: 4105.
    Returns: the total number of donuts Andrew ate in three days.
    """
    # L1
    donuts_monday = 14 # Andrew eats 14 donuts on Monday

    # L2
    half_divisor = 2 # half as many on Tuesday
    donuts_tuesday = donuts_monday / half_divisor

    # L3
    wednesday_multiplier = 4 # 4 times as many
    donuts_wednesday = wednesday_multiplier * donuts_tuesday

    # L4
    total_donuts = donuts_monday + donuts_tuesday + donuts_wednesday

    # FA
    answer = total_donuts
    return answer