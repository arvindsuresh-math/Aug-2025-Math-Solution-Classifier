def solve(
    hourly_wage: float = 18.00, # Tina makes $18.00 an hour
    regular_hours_per_shift: int = 8, # more than 8 hours per shift
    overtime_multiplier_fraction: float = 1/2, # paid by your hourly wage + 1/2 your hourly wage
    hours_worked_per_day: int = 10, # works 10 hours every day
    num_days: int = 5 # for 5 days
):
    """Index: 9.
    Returns: the total money Tina makes over 5 days including overtime.
    """

    #: L1
    regular_shift_pay = regular_hours_per_shift * hourly_wage # eval: 144.0 = 8 * 18.0

    #: L2
    overtime_hours_per_day = hours_worked_per_day - regular_hours_per_shift # eval: 2 = 10 - 8

    #: L3
    overtime_extra_per_hour = hourly_wage * overtime_multiplier_fraction # eval: 9.0 = 18.0 * 0.5

    #: L4
    overtime_rate = hourly_wage + overtime_extra_per_hour # eval: 27.0 = 18.0 + 9.0

    #: L5
    total_base_pay = regular_shift_pay * num_days # eval: 720.0 = 144.0 * 5

    #: L6
    overtime_pay_per_day = overtime_rate * overtime_hours_per_day # eval: 54.0 = 27.0 * 2

    #: L7
    total_overtime_pay = overtime_pay_per_day * num_days # eval: 270.0 = 54.0 * 5

    #: L8
    total_pay = 980.0 # eval: 980.0 = 980.0

    #: FA
    answer = total_pay
    return answer # eval: return 980.0
