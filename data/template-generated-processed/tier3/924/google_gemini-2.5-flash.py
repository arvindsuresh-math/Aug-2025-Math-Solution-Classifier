def solve():
    """Index: 924.
    Returns: the total time in hours to complete the laundry.
    """
    # L1
    dry_cycle_minutes = 60 # 1 hour in the dry cycle
    wash_cycle_minutes = 45 # 45 minutes to complete in the wash cycle
    minutes_per_load = dry_cycle_minutes + wash_cycle_minutes

    # L2
    num_loads = 8 # 8 loads of laundry
    total_minutes = num_loads * minutes_per_load

    # L3
    minutes_in_hour = 60 # WK
    total_hours = total_minutes / minutes_in_hour

    # FA
    answer = total_hours
    return answer