def solve():
    """Index: 2268.
    Returns: the number of toads Kevin has in his shoebox.
    """
    # L1
    time_per_worm_minutes = 15 # 15 minutes to find each worm
    minutes_per_hour = 60 # WK
    worms_per_hour = minutes_per_hour / time_per_worm_minutes

    # L2
    total_time_hours = 6 # 6 hours to find enough worms
    total_worms_caught = worms_per_hour * total_time_hours

    # L3
    worms_per_toad = 3 # feeds each toad 3 worms
    number_of_toads = total_worms_caught / worms_per_toad

    # FA
    answer = number_of_toads
    return answer