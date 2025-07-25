def solve():
    """Index: 3917.
    Returns: the total number of hours Jack had to wait.
    """
    # L1
    quarantine_days = 14 # 14 days in coronavirus quarantine
    hours_per_day = 24 # WK
    quarantine_hours = quarantine_days * hours_per_day

    # L2
    customs_wait_hours = 20 # 20 hours to get through customs
    total_wait_hours = quarantine_hours + customs_wait_hours

    # FA
    answer = total_wait_hours
    return answer