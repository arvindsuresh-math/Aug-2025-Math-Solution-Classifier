def solve():
    """Index: 1822.
    Returns: the total distance the ship has traveled in the three days.
    """
    # L1
    distance_north_day1 = 100 # 100 miles north on the first day
    multiplier_east_day2 = 3 # three times as far as the distance as he covered on the first day
    distance_east_day2 = multiplier_east_day2 * distance_north_day1

    # L2
    additional_east_day3 = 110 # 110 more miles than the distance it covered on the second day
    distance_east_day3 = distance_east_day2 + additional_east_day3

    # L3
    total_distance = distance_east_day3 + distance_east_day2 + distance_north_day1

    # FA
    answer = total_distance
    return answer