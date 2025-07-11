def solve(
    base_income: int = 500, # Irene earns $500
    base_hours: int = 40, # if she works for 40 hours a week
    overtime_rate: int = 20, # and gets an extra $20 for every hour of overtime
    hours_worked: int = 50 # If she worked 50 hours last week
):
    """Index: 82.
    Returns: Irene's total income for the week.
    """
    #: L1
    overtime_hours = hours_worked - base_hours

    #: L2
    overtime_income = overtime_hours * overtime_rate

    #: L3
    total_income = base_income + overtime_income

    answer = total_income # FINAL ANSWER
    return answer