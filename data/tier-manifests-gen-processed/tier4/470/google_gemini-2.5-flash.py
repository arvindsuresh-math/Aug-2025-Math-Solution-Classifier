def solve():
    """Index: 470.
    Returns: the total number of hours Gary worked that week.
    """
    # L1
    normal_hours_threshold = 40 # every hour after 40
    normal_wage_per_hour = 12 # Gary normally earns $12 per hour
    normal_wage_earnings = normal_hours_threshold * normal_wage_per_hour

    # L2
    total_paycheck = 696 # His paycheck (before taxes are taken out) came out to $696
    overtime_earnings = total_paycheck - normal_wage_earnings

    # L3
    overtime_multiplier = 1.5 # 1.5 times his normal wage
    overtime_wage_per_hour = normal_wage_per_hour * overtime_multiplier

    # L4
    overtime_hours = overtime_earnings / overtime_wage_per_hour

    # L5
    total_hours_worked = normal_hours_threshold + overtime_hours

    # FA
    answer = total_hours_worked
    return answer