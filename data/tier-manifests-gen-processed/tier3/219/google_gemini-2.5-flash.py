def solve():
    """Index: 219.
    Returns: the number of hotdogs Lisa needs to eat per minute.
    """
    # L1
    joey_chestnut_record = 75 # Joey Chestnut's record of eating 75 full hotdogs
    lisa_eaten_hotdogs = 20 # Lisa has eaten 20 hotdogs
    hotdogs_needed = joey_chestnut_record - lisa_eaten_hotdogs

    # L2
    total_time_minutes = 10 # in 10 minutes
    time_divisor = 2 # Halfway through the time
    minutes_left = total_time_minutes / time_divisor

    # L3
    hotdogs_per_minute = hotdogs_needed / minutes_left

    # FA
    answer = hotdogs_per_minute
    return answer