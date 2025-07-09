def solve(
    hourly_wage: float = 18.00, # Tina makes $18.00 an hour.
    hours_per_shift: int = 10, # If she works 10 hours every day
    days_worked: int = 5 # for 5 days
):
    """Index: 9.
    Returns: the total amount of money Tina makes.
    """
    #: L1
    regular_hours_per_shift = 8 # If she works more than 8 hours per shift
    base_pay_per_shift = regular_hours_per_shift * hourly_wage

    #: L2
    overtime_hours_per_shift = hours_per_shift - regular_hours_per_shift

    #: L3
    overtime_rate_increase = hourly_wage * 0.5

    #: L4
    overtime_hourly_wage = hourly_wage + overtime_rate_increase

    #: L5
    total_base_pay = base_pay_per_shift * days_worked

    #: L6
    overtime_pay_per_shift = overtime_hours_per_shift * overtime_hourly_wage

    #: L7
    total_overtime_pay = overtime_pay_per_shift * days_worked

    #: L8
    total_earnings = total_base_pay + total_overtime_pay

    answer = total_earnings # FINAL ANSWER
    return answer