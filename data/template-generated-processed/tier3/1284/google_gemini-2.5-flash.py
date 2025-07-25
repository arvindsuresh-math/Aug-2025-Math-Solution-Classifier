def solve():
    """Index: 1284.
    Returns: the total amount of water used in 4 weeks.
    """
    # L1
    num_weeks = 4 # for 4 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L2
    shower_frequency_divisor = 2 # every other day
    num_showers = total_days / shower_frequency_divisor

    # L3
    shower_duration_minutes = 10 # 10-minute shower
    total_shower_minutes = num_showers * shower_duration_minutes

    # L4
    water_per_minute = 2 # uses 2 gallons of water per minute
    total_water_gallons = water_per_minute * total_shower_minutes

    # FA
    answer = total_water_gallons
    return answer