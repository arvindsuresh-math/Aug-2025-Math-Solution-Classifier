def solve():
    """Index: 1419.
    Returns: the number of kilometers Arvin ran on the 5th day.
    """
    # L1
    day1_km = 2 # On the first day, he ran 2 kilometers
    daily_increase = 1 # increased his running distance by 1 kilometer over the previous day
    day2_km = day1_km + daily_increase

    # L2
    day3_km = day2_km + daily_increase

    # L3
    day4_km = day3_km + daily_increase

    # L4
    day5_km = day4_km + daily_increase

    # FA
    answer = day5_km
    return answer