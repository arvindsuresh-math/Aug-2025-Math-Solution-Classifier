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
    regular_pay_per_shift = regular_hours_per_shift * hourly_wage # eval: 144.0 = 8 * 18.0

    #: L2
    overtime_hours_per_day = hours_per_day - regular_hours_per_shift # eval: 2 = 10 - 8

    #: L3
    overtime_rate_increase = hourly_wage * overtime_multiplier # eval: 9.0 = 18.0 * 0.5

    #: L4
    overtime_hourly_rate = hourly_wage + overtime_rate_increase # eval: 27.0 = 18.0 + 9.0

    #: L5
    regular_pay_total = regular_pay_per_shift * days_worked # eval: 720.0 = 144.0 * 5

    #: L6
    overtime_pay_per_day = overtime_hourly_rate * overtime_hours_per_day # eval: 54.0 = 27.0 * 2

    #: L7
    overtime_pay_total = overtime_pay_per_day * days_worked # eval: 270.0 = 54.0 * 5

    #: L8
    total_earnings = regular_pay_total - overtime_pay_total # eval: 450.0 = 720.0 - 270.0

    #: FA
    answer = total_earnings
    return answer # eval: return 450.0
