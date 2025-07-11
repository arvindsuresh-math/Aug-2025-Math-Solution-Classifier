def solve():
    """Index: 370.
    Returns: the total time in minutes for Missy to serve dinner to all patients.
    """
    # L1
    total_patients = 12 # 12 patients in her hospital ward
    special_fraction = 1/3 # one-third of her patients have special dietary requirements
    special_patients = total_patients * special_fraction

    # L2
    standard_patients = total_patients - special_patients

    # L3
    percent_longer = 0.20 # increases the serving time by 20%
    standard_time = 5 # 5 minutes to serve each standard care patient
    special_time = (1 + percent_longer) * standard_time

    # L4
    standard_total_time = standard_time * standard_patients

    # L5
    special_total_time = special_time * special_patients

    # L6
    total_time = standard_total_time + special_total_time

    # FA
    answer = total_time
    return answer