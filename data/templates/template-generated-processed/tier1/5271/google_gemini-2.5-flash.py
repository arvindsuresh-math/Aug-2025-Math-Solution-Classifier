def solve():
    """Index: 5271.
    Returns: the total number of days the duck is flying during these seasons.
    """
    # L1
    days_to_south_winter = 40 # 40 days to fly to the south during winter
    multiplier_for_north = 2 # twice as much time
    days_to_north_summer = days_to_south_winter * multiplier_for_north

    # L2
    total_south_north = days_to_north_summer + days_to_south_winter

    # L3
    days_to_east_spring = 60 # 60 days to travel to the East during spring
    total_flying_days = total_south_north + days_to_east_spring

    # FA
    answer = total_flying_days
    return answer