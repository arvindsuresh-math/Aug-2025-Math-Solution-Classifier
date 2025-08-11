def solve():
    """Index: 1426.
    Returns: the number of clerks that must be hired.
    """
    # L1
    forms_per_hour_per_clerk = 25 # 25 forms per hour
    hours_in_day = 8 # 8-hour day
    forms_per_clerk_per_day = forms_per_hour_per_clerk * hours_in_day

    # L2
    total_forms_needed = 2400 # 2400 forms must be processed
    clerks_needed = total_forms_needed / forms_per_clerk_per_day

    # FA
    answer = clerks_needed
    return answer