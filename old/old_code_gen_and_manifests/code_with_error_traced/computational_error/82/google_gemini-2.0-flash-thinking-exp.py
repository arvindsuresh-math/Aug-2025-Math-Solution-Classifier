def solve(
    base_income: int = 500, # Irene earns $500
    base_hours: int = 40, # if she works for 40 hours a week
    overtime_rate: int = 20, # gets an extra $20 for every hour of overtime
    hours_worked: int = 50 # If she worked 50 hours last week
):
    """Index: 82.
    Returns: Irene's total income for the week.
    """

    #: L1
    overtime_hours = hours_worked - base_hours # eval: 10 = 50 - 40

    #: L2
    overtime_pay = 190 # eval: 190 = 190

    #: L3
    total_income = base_income + overtime_pay # eval: 690 = 500 + 190

    #: FA
    answer = total_income
    return answer # eval: return 690
