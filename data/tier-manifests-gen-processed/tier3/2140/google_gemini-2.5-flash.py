def solve():
    """Index: 2140.
    Returns: the total mg of Tylenol James takes a day.
    """
    # L1
    tablet_strength = 375 # 375 mg each
    num_tablets_per_dose = 2 # 2 Tylenol tablets
    mg_per_dose = tablet_strength * num_tablets_per_dose

    # L2
    hours_per_day = 24 # WK
    dose_interval_hours = 6 # every 6 hours
    num_doses_per_day = hours_per_day / dose_interval_hours

    # L3
    total_mg_per_day = mg_per_dose * num_doses_per_day

    # FA
    answer = total_mg_per_day
    return answer