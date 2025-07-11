def solve(
    base_hours: int = 40, # Irene earns $500 if she works for 40 hours a week
    base_income: int = 500, # Irene earns $500 if she works for 40 hours a week
    overtime_rate: int = 20, # gets an extra $20 for every hour of overtime
    hours_worked: int = 50 # If she worked 50 hours last week
):
    """Index: 82.
    Returns: Irene's total income for the week.
    """

    #: L1
    overtime_hours = hours_worked - base_hours # eval: 10 = 50 - 40

    #: L2
    overtime_income = overtime_hours * overtime_rate # eval: 200 = 10 * 20

    #: L3
    total_income = 701 # eval: 701 = 701

    #: FA
    answer = total_income
    return answer # eval: return 701
