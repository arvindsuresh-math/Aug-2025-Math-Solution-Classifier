def solve():
    """Index: 7467.
    Returns: the amount of time, in hours, it will take for the air conditioner to restore the warehouse to its previous temperature.
    """
    # L1
    power_out_duration = 3 # three hours
    temp_rise_rate = 8 # 8 degrees per hour
    total_temp_rise = power_out_duration * temp_rise_rate

    # L2
    temp_lower_rate = 4 # 4 degrees F per hour
    time_to_restore = total_temp_rise / temp_lower_rate

    # FA
    answer = time_to_restore
    return answer