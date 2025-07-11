def solve():
    """Index: 947.
    Returns: the number of additional days Johnny needs to practice to reach three times his current practice.
    """
    # L1
    days_ago_state = 20 # 20 days ago
    factor_from_half_practice = 2 # half as much practice as he has currently (meaning current is 2 times past)
    current_practice_duration_days = days_ago_state * factor_from_half_practice

    # L2
    target_practice_multiplier = 3 # 3 times as much practice
    required_total_practice_days = current_practice_duration_days * target_practice_multiplier

    # L3
    additional_days_needed = required_total_practice_days - current_practice_duration_days

    # FA
    answer = additional_days_needed
    return answer