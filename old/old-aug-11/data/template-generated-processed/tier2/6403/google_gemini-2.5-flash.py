def solve():
    """Index: 6403.
    Returns: the amount the archer spends for arrows a week.
    """
    # L1
    shots_per_day = 200 # shoot 200 shots
    days_per_week = 4 # 4 days a week
    total_shots_per_week = shots_per_day * days_per_week

    # L2
    recovery_rate = 0.2 # recover 20% of his arrows
    recovered_arrows = total_shots_per_week * recovery_rate

    # L3
    arrows_used_per_week = total_shots_per_week - recovered_arrows

    # L4
    cost_per_arrow = 5.5 # cost $5.5 per arrow
    total_cost_before_team_contribution = arrows_used_per_week * cost_per_arrow

    # L5
    team_contribution_rate = 0.7 # pay for 70% of the cost of his arrows
    team_paid_amount = total_cost_before_team_contribution * team_contribution_rate

    # L6
    archer_cost_per_week = total_cost_before_team_contribution - team_paid_amount

    # FA
    answer = archer_cost_per_week
    return answer