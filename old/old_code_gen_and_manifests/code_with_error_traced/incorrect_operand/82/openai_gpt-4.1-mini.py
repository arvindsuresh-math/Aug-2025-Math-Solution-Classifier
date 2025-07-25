def solve(
    base_income: int = 500,  # Irene earns $500 if she works for 40 hours a week
    base_hours: int = 40,    # 40 hours a week
    overtime_rate: int = 20, # gets an extra $20 for every hour of overtime
    hours_worked: int = 50   # she worked 50 hours last week
):
    """Index: 82.
    Returns: Irene's total income including overtime pay.
    """

    #: L1
    overtime_hours = hours_worked - hours_worked # eval: 0 = 50 - 50

    #: L2
    overtime_pay = overtime_hours * overtime_rate # eval: 0 = 0 * 20

    #: L3
    total_income = base_income + overtime_pay # eval: 500 = 500 + 0

    #: FA
    answer = total_income
    return answer # eval: return 500
