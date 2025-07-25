def solve():
    """Index: 4294.
    Returns: the total money Sarah has saved over 12 weeks.
    """
    # L1
    weekly_savings_phase1 = 5.00 # $5.00 a week
    duration_phase1 = 4 # 4 weeks
    savings_phase1 = weekly_savings_phase1 * duration_phase1

    # L2
    weekly_savings_phase2 = 10.00 # $10.00 a week
    duration_phase2 = 4 # 4 weeks
    savings_phase2 = weekly_savings_phase2 * duration_phase2

    # L3
    weekly_savings_phase3 = 20.00 # $20.00 a week
    duration_phase3 = 4 # 4 weeks
    savings_phase3 = weekly_savings_phase3 * duration_phase3

    # L4
    total_savings = savings_phase1 + savings_phase2 + savings_phase3

    # FA
    answer = total_savings
    return answer