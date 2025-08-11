def solve():
    """Index: 6390.
    Returns: the total liters of water Ivar needs for all horses for 28 days.
    """
    # L1
    initial_horses = 3 # 3 horses
    added_horses = 5 # added 5 horses
    total_horses = added_horses + initial_horses

    # L2
    water_drinking_per_horse = 5 # 5 liters of water for drinking
    water_bathing_per_horse = 2 # 2 liters for bathing
    water_per_horse_per_day = water_drinking_per_horse + water_bathing_per_horse

    # L3
    total_water_per_day = water_per_horse_per_day * total_horses

    # L4
    days_per_week = 7 # WK
    total_water_per_week = total_water_per_day * days_per_week

    # L5
    num_days_for_period = 28 # for 28 days
    num_weeks_in_period = num_days_for_period / days_per_week
    total_water_for_period = total_water_per_week * num_weeks_in_period

    # FA
    answer = total_water_for_period
    return answer