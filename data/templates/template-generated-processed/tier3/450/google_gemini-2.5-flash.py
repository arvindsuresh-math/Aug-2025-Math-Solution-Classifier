def solve():
    """Index: 450.
    Returns: the additional gallons of milk Flora must drink daily.
    """
    # L1
    weeks = 3 # 3 weeks
    days_per_week = 7 # WK
    total_days = weeks * days_per_week

    # L2
    total_milk_gallons = 105 # 105 gallons of milk
    required_daily_milk = total_milk_gallons / total_days

    # L3
    flora_daily_milk = 3 # drinking 3 gallons of milk daily
    additional_daily_milk_needed = required_daily_milk - flora_daily_milk

    # FA
    answer = additional_daily_milk_needed
    return answer