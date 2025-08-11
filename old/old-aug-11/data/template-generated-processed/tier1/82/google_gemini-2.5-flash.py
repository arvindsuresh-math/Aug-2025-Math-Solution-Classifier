def solve():
    """Index: 82.
    Returns: Irene's total income.
    """
    # L1
    total_hours_worked = 50 # worked 50 hours last week
    regular_hours = 40 # works for 40 hours a week
    overtime_hours = total_hours_worked - regular_hours

    # L2
    overtime_rate = 20 # gets an extra $20 for every hour of overtime
    overtime_income = overtime_hours * overtime_rate

    # L3
    base_income = 500 # earns $500 if she works for 40 hours a week
    total_income = base_income + overtime_income

    # FA
    answer = total_income
    return answer