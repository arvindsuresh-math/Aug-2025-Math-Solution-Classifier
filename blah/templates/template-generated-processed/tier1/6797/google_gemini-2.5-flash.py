def solve():
    """Index: 6797.
    Returns: the combined total number of sit-ups performed.
    """
    # L1
    barney_situps_per_minute = 45 # Barney can perform 45 sit-ups in one minute.
    carrie_multiplier = 2 # twice as many sit-ups per minute as Barney can.
    carrie_situps_per_minute = carrie_multiplier * barney_situps_per_minute

    # L2
    jerrie_extra_situps = 5 # 5 more sit-ups per minute than Carrie can do.
    jerrie_situps_per_minute = carrie_situps_per_minute + jerrie_extra_situps

    # L3
    carrie_minutes = 2 # Carrie does sit-ups for two minutes
    carrie_total_situps = carrie_situps_per_minute * carrie_minutes

    # L4
    jerrie_minutes = 3 # Jerrie does sit-ups for three minutes
    jerrie_total_situps = jerrie_minutes * jerrie_situps_per_minute

    # L5
    combined_total_situps = barney_situps_per_minute + carrie_total_situps + jerrie_total_situps

    # FA
    answer = combined_total_situps
    return answer