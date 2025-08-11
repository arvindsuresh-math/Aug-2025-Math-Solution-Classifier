def solve():
    """Index: 438.
    Returns: how much less rain Greg experienced while camping compared to his house.
    """
    # L1
    rain_day1 = 3 # amount of rain was 3 mm
    rain_day2 = 6 # amount of rain was 6 mm
    rain_day3 = 5 # amount of rain was 5 mm
    total_rain_camping = rain_day1 + rain_day2 + rain_day3

    # L2
    rain_at_house = 26 # it rained 26 mm at his house
    less_rain_camping = rain_at_house - total_rain_camping

    # FA
    answer = less_rain_camping
    return answer