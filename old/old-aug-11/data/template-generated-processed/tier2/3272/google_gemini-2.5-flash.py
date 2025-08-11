def solve():
    """Index: 3272.
    Returns: the total amount of water John saved in June.
    """
    # L1
    gallons_per_flush_old = 5 # uses 5 gallons of water per flush
    flushes_per_day = 15 # flushed 15 times per day
    old_daily_usage = gallons_per_flush_old * flushes_per_day

    # L2
    days_in_june = 30 # WK
    old_monthly_usage = old_daily_usage * days_in_june

    # L3
    water_reduction_percent = 0.8 # uses 80% less water per flush
    water_saved_per_flush = gallons_per_flush_old * water_reduction_percent

    # L4
    new_gallons_per_flush = gallons_per_flush_old - water_saved_per_flush

    # L5
    new_daily_usage = new_gallons_per_flush * flushes_per_day

    # L6
    new_monthly_usage = new_daily_usage * days_in_june

    # L7
    total_saved_water = old_monthly_usage - new_monthly_usage

    # FA
    answer = total_saved_water
    return answer