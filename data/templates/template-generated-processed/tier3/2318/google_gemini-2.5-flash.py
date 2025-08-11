def solve():
    """Index: 2318.
    Returns: the total hours to dry all of the dogs.
    """
    # L1
    short_hair_dry_time_minutes = 10 # 10 minutes to dry a short-haired dog
    full_hair_multiplier = 2 # twice as long
    full_hair_dry_time_minutes = short_hair_dry_time_minutes * full_hair_multiplier

    # L2
    num_short_hair_dogs = 6 # 6 short-haired dogs
    total_short_hair_dry_time_minutes = num_short_hair_dogs * short_hair_dry_time_minutes

    # L3
    num_full_hair_dogs = 9 # 9 full-haired dogs
    total_full_hair_dry_time_minutes = num_full_hair_dogs * full_hair_dry_time_minutes

    # L4
    total_dry_time_minutes = total_short_hair_dry_time_minutes + total_full_hair_dry_time_minutes

    # L5
    minutes_per_hour = 60 # WK
    hours_in_one_hour = 1 # WK
    total_dry_time_hours = total_dry_time_minutes / minutes_per_hour

    # FA
    answer = total_dry_time_hours
    return answer