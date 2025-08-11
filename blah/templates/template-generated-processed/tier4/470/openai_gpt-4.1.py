def solve():
    """Index: 470.
    Returns: the total number of hours Gary worked that week.
    """
    # L1
    regular_hours = 40 # every hour after 40 is overtime
    normal_wage = 12 # Gary normally earns $12 per hour
    regular_pay = regular_hours * normal_wage

    # L2
    total_pay = 696 # His paycheck (before taxes) came out to $696
    overtime_pay = total_pay - regular_pay

    # L3
    overtime_multiplier = 1.5 # 1.5 times his normal wage
    overtime_wage = normal_wage * overtime_multiplier

    # L4
    overtime_hours = overtime_pay / overtime_wage

    # L5
    total_hours = regular_hours + overtime_hours

    # FA
    answer = total_hours
    return answer