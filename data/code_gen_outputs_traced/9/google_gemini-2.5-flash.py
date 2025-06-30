def solve(
        hourly_wage: float = 18.00, # Tina makes $18.00 an hour
        standard_shift_hours: int = 8, # more than 8 hours per shift
        overtime_multiplier_fraction: float = 1/2, # 1/2 your hourly wage
        daily_work_hours: int = 10, # 10 hours every day
        num_work_days: int = 5 # for 5 days
    ):
    """Index: 9.
    Returns: the total money Tina makes for working 10 hours every day for 5 days.
    """

    #: L1
    standard_daily_pay = standard_shift_hours * hourly_wage # eval: 144.0 = 8 * 18.0

    #: L2
    overtime_hours_per_day = daily_work_hours - standard_shift_hours # eval: 2 = 10 - 8

    #: L3
    overtime_extra_per_hour = hourly_wage * overtime_multiplier_fraction # eval: 9.0 = 18.0 * 0.5

    #: L4
    overtime_hourly_rate = hourly_wage + overtime_extra_per_hour # eval: 27.0 = 18.0 + 9.0

    #: L5
    total_base_pay_5_days = standard_daily_pay * num_work_days # eval: 720.0 = 144.0 * 5

    #: L6
    daily_overtime_pay = overtime_hourly_rate * overtime_hours_per_day # eval: 54.0 = 27.0 * 2

    #: L7
    total_overtime_pay_5_days = daily_overtime_pay * num_work_days # eval: 270.0 = 54.0 * 5

    #: L8
    total_earnings = total_base_pay_5_days + total_overtime_pay_5_days # eval: 990.0 = 720.0 + 270.0

    #: FA
    answer = total_earnings # eval: 990.0 = 990.0
    return answer # eval: return 990.0
