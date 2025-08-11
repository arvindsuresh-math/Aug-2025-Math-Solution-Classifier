def solve():
    """Index: 6427.
    Returns: the total number of days John spends on jury duty.
    """
    # L1
    full_deliberation_days = 6 # 6 full days
    hours_per_day = 24 # WK
    total_deliberation_hours = full_deliberation_days * hours_per_day

    # L2
    hours_per_day_deliberation = 16 # 16 hours a day in deliberation
    actual_deliberation_days = total_deliberation_hours / hours_per_day_deliberation

    # L3
    jury_selection_days = 2 # Jury selection takes 2 days
    trial_duration_multiplier = 4 # lasts 4 times as long as jury selection
    trial_days = jury_selection_days * trial_duration_multiplier

    # L4
    total_jury_duty_days = jury_selection_days + trial_days + actual_deliberation_days

    # FA
    answer = total_jury_duty_days
    return answer