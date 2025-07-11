def solve():
    """Index: 396.
    Returns: the total number of pills Holly takes in a week.
    """
    # L1
    blood_pressure_per_day = 3 # 3 blood pressure pills per day
    multiplier_anticonvulsant = 2 # twice as many anticonvulsants as blood pressure pills
    anticonvulsant_per_day = blood_pressure_per_day * multiplier_anticonvulsant

    # L2
    insulin_per_day = 2 # 2 insulin pills per day
    total_per_day = anticonvulsant_per_day + insulin_per_day + blood_pressure_per_day

    # L3
    days_in_week = 7 # WK
    total_per_week = total_per_day * days_in_week

    # FA
    answer = total_per_week
    return answer