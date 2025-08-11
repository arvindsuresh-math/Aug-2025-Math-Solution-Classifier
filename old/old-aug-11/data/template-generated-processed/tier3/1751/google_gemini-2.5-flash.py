def solve():
    """Index: 1751.
    Returns: the number of days of rain the sewers can handle.
    """
    # L1
    sewer_capacity_gallons = 240000 # 240,000 gallons of run-off
    runoff_per_hour = 1000 # 1000 gallons of runoff
    hours_sewers_can_handle = sewer_capacity_gallons / runoff_per_hour

    # L2
    hours_per_day = 24 # WK
    days_sewers_can_handle = hours_sewers_can_handle / hours_per_day

    # FA
    answer = days_sewers_can_handle
    return answer