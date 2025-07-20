def solve():
    """Index: 3247.
    Returns: the total time taken to recover from everything.
    """
    # L1
    initial_healing_weeks = 4 # 4 weeks to heal enough
    longer_percentage_decimal = 0.5 # 50% longer
    skin_graft_extra_healing_weeks = initial_healing_weeks * longer_percentage_decimal

    # L2
    skin_graft_total_healing_weeks = initial_healing_weeks + skin_graft_extra_healing_weeks

    # L3
    total_recovery_weeks = initial_healing_weeks + skin_graft_total_healing_weeks

    # FA
    answer = total_recovery_weeks
    return answer