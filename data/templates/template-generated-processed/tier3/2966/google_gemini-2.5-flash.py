def solve():
    """Index: 2966.
    Returns: the total grams of Tylenol taken.
    """
    # L1
    total_hours = 12 # for 12 hours
    dose_interval_hours = 4 # every 4 hours
    num_doses = total_hours / dose_interval_hours

    # L2
    mg_per_tablet = 500 # 500 mg each
    tablets_per_dose = 2 # 2 Tylenol tablets
    mg_per_dose = mg_per_tablet * tablets_per_dose

    # L3
    total_mg = num_doses * mg_per_dose

    # L4
    mg_per_gram = 1000 # WK
    total_grams = total_mg / mg_per_gram

    # FA
    answer = total_grams
    return answer