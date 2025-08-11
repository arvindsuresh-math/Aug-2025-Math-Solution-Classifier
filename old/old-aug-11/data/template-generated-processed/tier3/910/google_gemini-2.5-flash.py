def solve():
    """Index: 910.
    Returns: the number of cups of coffee John drinks a day.
    """
    # L1
    ounces_per_gallon = 128 # WK
    jug_fraction_denominator = 2 # 1/2 gallon jugs
    ounces_per_jug_4_days = ounces_per_gallon / jug_fraction_denominator

    # L2
    days_per_jug = 4 # every 4 days
    daily_ounces = ounces_per_jug_4_days / days_per_jug

    # L3
    ounces_per_cup = 8 # WK
    daily_cups = daily_ounces / ounces_per_cup

    # FA
    answer = daily_cups
    return answer