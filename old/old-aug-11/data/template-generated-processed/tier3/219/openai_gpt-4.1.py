def solve():
    """Index: 219.
    Returns: the number of hotdogs Lisa must eat per minute to tie the record.
    """
    # L1
    record_hotdogs = 75 # Joey Chestnut's record of eating 75 full hotdogs
    hotdogs_eaten_so_far = 20 # Lisa has eaten 20 hot dogs so far
    hotdogs_needed = record_hotdogs - hotdogs_eaten_so_far

    # L2
    total_time_minutes = 10 # 10 minute time period
    time_divisor = 2 # Halfway through the time
    minutes_left = total_time_minutes / time_divisor

    # L3
    hotdogs_per_minute = hotdogs_needed / minutes_left

    # FA
    answer = hotdogs_per_minute
    return answer