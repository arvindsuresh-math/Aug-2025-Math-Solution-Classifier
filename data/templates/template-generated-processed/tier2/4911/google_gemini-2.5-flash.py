def solve():
    """Index: 4911.
    Returns: the final weight of Ajax in pounds after exercising.
    """
    # L1
    ajax_weight_kg = 80 # Ajax is 80 kilograms
    kg_to_lbs_conversion = 2.2 # 1 kilogram is equal to 2.2 pounds
    ajax_weight_lbs = ajax_weight_kg * kg_to_lbs_conversion

    # L2
    pounds_lost_per_hour = 1.5 # lose 1.5 pounds
    exercise_hours_per_day = 2 # exercises for 2 hours every day
    pounds_lost_per_day = pounds_lost_per_hour * exercise_hours_per_day

    # L3
    days_per_week = 7 # WK
    pounds_lost_per_week = pounds_lost_per_day * days_per_week

    # L4
    num_weeks = 2 # two weeks
    total_pounds_lost = pounds_lost_per_week * num_weeks

    # L5
    final_weight_lbs = ajax_weight_lbs - total_pounds_lost

    # FA
    answer = final_weight_lbs
    return answer