def solve():
    """Index: 4002.
    Returns: the total number of pills taken.
    """
    # L1
    dosage_mg = 1000 # 1000 mg
    pill_strength_mg = 500 # each 500 mg
    pills_per_dose = dosage_mg / pill_strength_mg

    # L2
    hours_per_day = 24 # WK
    dose_interval_hours = 6 # every 6 hours
    doses_per_day = hours_per_day / dose_interval_hours

    # L3
    pills_per_day = doses_per_day * pills_per_dose

    # L4
    num_weeks = 2 # 2 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L5
    total_pills = pills_per_day * total_days

    # FA
    answer = total_pills
    return answer