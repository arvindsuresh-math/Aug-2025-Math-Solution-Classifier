def solve(
    hourly_wage: float = 18.00, # Tina makes $18.00 an hour.
    regular_hours_per_shift: int = 8, # If she works more than 8 hours per shift
    overtime_multiplier: float = 0.5, # overtime, which is paid by your hourly wage + 1/2 your hourly wage.
    hours_per_day: int = 10, # If she works 10 hours every day
    days_worked: int = 5 # for 5 days
):
    """Index: 9.
    Returns: the total amount of money Tina makes.
    """

    #: L1
    regular_pay_per_shift = regular_hours_per_shift * hourly_wage

    #: L2

    #: L3
    overtime_rate_increase = hourly_wage * overtime_multiplier

    #: L4
    overtime_hourly_rate = hourly_wage + overtime_rate_increase

    #: L5
    regular_pay_total = regular_pay_per_shift * days_worked

    #: L6
    overtime_pay_per_day = overtime_hourly_rate * hourly_wage

    #: L7
    overtime_pay_total = overtime_pay_per_day * days_worked

    #: L8
    total_earnings = regular_pay_total + overtime_pay_total

    #: FA
    answer = total_earnings
    return answer