def solve():
    """Index: 6242.
    Returns: the total amount of water Tim drinks a week in ounces.
    """
    # L1
    quarts_per_bottle = 1.5 # 1.5 quarts
    ounces_per_quart = 32 # WK
    ounces_per_bottle = quarts_per_bottle * ounces_per_quart

    # L2
    num_bottles = 2 # 2 bottles
    ounces_from_bottles_daily = ounces_per_bottle * num_bottles

    # L3
    additional_ounces_daily = 20 # additional 20 ounces a day
    total_ounces_daily = ounces_from_bottles_daily + additional_ounces_daily

    # L4
    days_per_week = 7 # WK
    total_ounces_weekly = total_ounces_daily * days_per_week

    # FA
    answer = total_ounces_weekly
    return answer