def solve():
    """Index: 4480.
    Returns: the total ounces of cleaner used after 30 minutes.
    """
    # L1
    initial_flow_rate = 2 # 2 ounces of cleaner can run through the pipe per minute
    initial_time = 15 # After fifteen minutes
    ounces_used_phase1 = initial_flow_rate * initial_time

    # L2
    next_flow_rate = 3 # 3 ounces can run through per minute
    next_time = 10 # Ten minutes later
    ounces_used_phase2 = next_flow_rate * next_time

    # L3
    total_time = 30 # after 30 minutes
    remaining_minutes = total_time - initial_time - next_time

    # L4
    final_flow_rate = 4 # 4 ounces to run through per minute
    ounces_used_phase3 = final_flow_rate * remaining_minutes

    # L5
    total_ounces_used = ounces_used_phase1 + ounces_used_phase2 + ounces_used_phase3

    # FA
    answer = total_ounces_used
    return answer