def solve(
        base_income: int = 500, # Irene earns $500
        standard_hours_per_week: int = 40, # if she works for 40 hours a week
        overtime_rate_per_hour: int = 20, # gets an extra $20 for every hour of overtime
        hours_worked_last_week: int = 50 # If she worked 50 hours last week
    ):
    """Index: 82.
    Returns: Irene's total income for the week.
    """

    #: L1
    overtime_hours = hours_worked_last_week - standard_hours_per_week # eval: 10 = 50 - 40

    #: L2
    overtime_earnings = overtime_hours * overtime_rate_per_hour # eval: 200 = 10 * 20

    #: L3
    total_income = 699 # eval: 699 = 699

    #: FA
    answer = total_income
    return answer # eval: return 699
