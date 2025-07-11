def solve():
    """Index: 450.
    Returns: the number of additional gallons Flora must drink daily to meet Dr. Juan's requirement.
    """
    # L1
    weeks = 3 # 3 weeks
    days_per_week = 7 # WK
    total_days = weeks * days_per_week

    # L2
    total_gallons_required = 105 # 105 gallons of milk
    required_daily_gallons = total_gallons_required / total_days

    # L3
    flora_daily_gallons = 3 # drinking 3 gallons of milk daily
    additional_gallons_needed = required_daily_gallons - flora_daily_gallons

    # FA
    answer = additional_gallons_needed
    return answer