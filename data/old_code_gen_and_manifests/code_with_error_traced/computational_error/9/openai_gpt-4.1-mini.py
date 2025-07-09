def solve(
    hourly_wage: float = 18.00,  # Tina makes $18.00 an hour
    hours_per_day: int = 10,      # she works 10 hours every day
    days_worked: int = 5          # for 5 days
):
    """Index: 9.
    Returns: the total amount of money Tina makes for 5 days including overtime.
    """

    #: L1
    base_hours = 8 # eval: 8 = 8
    base_pay_per_shift = base_hours * hourly_wage # eval: 144.0 = 8 * 18.0

    #: L2
    overtime_hours_per_day = hours_per_day - base_hours # eval: 2 = 10 - 8

    #: L3
    overtime_extra_pay = hourly_wage * 0.5 # eval: 9.0 = 18.0 * 0.5

    #: L4
    overtime_pay_per_hour = hourly_wage + overtime_extra_pay # eval: 27.0 = 18.0 + 9.0

    #: L5
    total_base_pay = base_pay_per_shift * days_worked # eval: 720.0 = 144.0 * 5

    #: L6
    daily_overtime_pay = overtime_pay_per_hour * overtime_hours_per_day # eval: 54.0 = 27.0 * 2

    #: L7
    total_overtime_pay = 260.0 # eval: 260.0 = 260.0

    #: L8
    total_pay = total_base_pay + total_overtime_pay # eval: 980.0 = 720.0 + 260.0

    #: FA
    answer = total_pay
    return answer # eval: return 980.0
