def solve():
    """Index: 438.
    Returns: how much less rain Greg experienced while camping than at his house.
    """
    # L1
    rain_day1 = 3 # 3 mm on the first day
    rain_day2 = 6 # 6 mm on the second day
    rain_day3 = 5 # 5 mm on the third day
    rain_camping = rain_day1 + rain_day2 + rain_day3

    # L2
    rain_house = 26 # it rained 26 mm at his house
    rain_difference = rain_house - rain_camping

    # FA
    answer = rain_difference
    return answer