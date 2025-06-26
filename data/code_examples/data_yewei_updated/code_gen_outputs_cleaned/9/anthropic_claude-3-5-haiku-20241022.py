def solve(
    hourly_wage: float = 18.00,  # Tina makes $18.00 an hour
    regular_hours_per_shift: int = 8,  # regular hours per shift
    hours_worked_per_day: int = 10,  # she works 10 hours every day
    days_worked: int = 5  # for 5 days
):
    """Index: 9.
    Returns: the total amount of money Tina makes in 5 days.
    """
    #: L1
    base_pay_per_shift = hourly_wage * regular_hours_per_shift

    #: L2
    overtime_hours_per_day = hours_worked_per_day - regular_hours_per_shift

    #: L3
    overtime_rate = hourly_wage * 0.5

    #: L4
    overtime_hourly_rate = hourly_wage + overtime_rate

    #: L5
    base_pay_total = base_pay_per_shift * days_worked

    #: L6
    overtime_pay_per_day = overtime_hourly_rate * overtime_hours_per_day

    #: L7
    overtime_pay_total = overtime_pay_per_day * days_worked

    #: L8
    total_pay = base_pay_total + overtime_pay_total

    answer = total_pay  # FINAL ANSWER
    return answer