def solve():
    """Index: 6917.
    Returns: the average rainfall amount in inches.
    """
    # L1
    march_rain = 3.79 # 3.79 inches of rain in March
    april_rain = 4.5 # 4.5 inches of rain in April
    may_rain = 3.95 # 3.95 inches of rain in May
    june_rain = 3.09 # 3.09 inches of rain in June
    july_rain = 4.67 # 4.67 inches in July
    total_rain = march_rain + april_rain + may_rain + june_rain + july_rain

    # L2
    num_months = 5 # from March through July for a total of 5 months
    average_rainfall = total_rain / num_months

    # FA
    answer = average_rainfall
    return answer