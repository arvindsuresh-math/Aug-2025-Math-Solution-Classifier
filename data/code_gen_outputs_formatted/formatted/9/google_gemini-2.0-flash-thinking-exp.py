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
    regular_shift_pay = regular_hours_per_shift * hourly_wage

    #: L2
    overtime_hours_per_day = hours_worked_per_day - regular_hours_per_shift

    #: L3
    overtime_extra_per_hour = hourly_wage * overtime_multiplier_fraction

    #: L4
    overtime_rate = hourly_wage + overtime_extra_per_hour

    #: L5
    total_base_pay = regular_shift_pay * num_days

    #: L6
    overtime_pay_per_day = overtime_rate * overtime_hours_per_day

    #: L7
    total_overtime_pay = overtime_pay_per_day * num_days

    #: L8
    total_pay = total_base_pay + total_overtime_pay

    answer = total_pay # FINAL ANSWER
    return answer