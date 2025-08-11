def solve():
    """Index: 5606.
    Returns: the minutes of free time left after cleaning the apartment.
    """
    # L1
    num_cats = 3 # he has three cats
    minutes_per_cat = 5 # 5 minutes to brush each cat
    time_brushing_cats = num_cats * minutes_per_cat

    # L2
    time_vacuum = 45 # 45 minutes to vacuum the carpets
    time_dust = 60 # 60 minutes to dust the furniture
    time_mop = 30 # 30 minutes to mop the floors in his kitchen
    total_cleaning_time = time_vacuum + time_dust + time_mop + time_brushing_cats

    # L3
    minutes_per_hour = 60 # WK
    free_time_hours = 3 # 3 hours of free time available
    total_free_time_minutes = minutes_per_hour * free_time_hours

    # L4
    remaining_free_time = total_free_time_minutes - total_cleaning_time

    # FA
    answer = remaining_free_time
    return answer