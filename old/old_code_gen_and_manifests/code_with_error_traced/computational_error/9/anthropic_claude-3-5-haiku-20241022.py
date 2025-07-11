def solve(
        hourly_wage: float = 18.00,  # Tina makes $18.00 an hour
        regular_hours_per_shift: int = 8,  # regular hours per shift
        total_hours_per_shift: int = 10,  # she works 10 hours every day
        days_worked: int = 5  # for 5 days
    ):
    """Index: 9.
    Returns: the total amount of money Tina makes in 5 days.
    """

    #: L1
    base_pay_per_shift = hourly_wage * regular_hours_per_shift # eval: 144.0 = 18.0 * 8

    #: L2
    overtime_hours_per_shift = 3 # eval: 3 = 3

    #: L3
    overtime_rate = hourly_wage * 0.5 # eval: 9.0 = 18.0 * 0.5

    #: L4
    overtime_hourly_rate = hourly_wage + overtime_rate # eval: 27.0 = 18.0 + 9.0

    #: L5
    base_pay_total = base_pay_per_shift * days_worked # eval: 720.0 = 144.0 * 5

    #: L6
    overtime_pay_per_shift = overtime_hourly_rate * overtime_hours_per_shift # eval: 81.0 = 27.0 * 3

    #: L7
    overtime_pay_total = overtime_pay_per_shift * days_worked # eval: 405.0 = 81.0 * 5

    #: L8
    total_pay = base_pay_total + overtime_pay_total # eval: 1125.0 = 720.0 + 405.0

    #: FA
    answer = total_pay
    return answer # eval: return 1125.0
