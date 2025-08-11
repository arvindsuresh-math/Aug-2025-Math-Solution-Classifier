def solve():
    """Index: 7242.
    Returns: the total quarts of water John drinks a week.
    """
    # L1
    gallons_per_day = 1.5 # 1.5 gallons of water a day
    quarts_per_gallon = 4 # WK
    quarts_per_day = gallons_per_day * quarts_per_gallon

    # L2
    days_per_week = 7 # WK
    quarts_per_week = quarts_per_day * days_per_week

    # FA
    answer = quarts_per_week
    return answer