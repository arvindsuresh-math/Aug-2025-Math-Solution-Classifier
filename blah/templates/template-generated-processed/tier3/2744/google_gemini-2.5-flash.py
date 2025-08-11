def solve():
    """Index: 2744.
    Returns: the number of minutes it will take the dog to fetch the potato.
    """
    # L1
    yards_per_field = 200 # 200 yards long
    num_fields = 6 # 6 football fields
    total_distance_yards = yards_per_field * num_fields

    # L2
    feet_per_yard = 3 # WK
    total_distance_feet = total_distance_yards * feet_per_yard

    # L3
    dog_speed_feet_per_minute = 400 # 400 feet/minute
    time_to_fetch_minutes = total_distance_feet / dog_speed_feet_per_minute

    # FA
    answer = time_to_fetch_minutes
    return answer