def solve():
    """Index: 1822.
    Returns: the total distance the ship has traveled in the three days.
    """
    # L1
    day1_north = 100 # 100 miles north on the first day
    day2_multiplier = 3 # three times as far as the distance as he covered on the first day
    day2_east = day2_multiplier * day1_north

    # L2
    day3_extra = 110 # 110 more miles than the distance it covered on the second day
    day3_east = day2_east + day3_extra

    # L3
    total_distance = day3_east + day2_east + day1_north

    # FA
    answer = total_distance
    return answer