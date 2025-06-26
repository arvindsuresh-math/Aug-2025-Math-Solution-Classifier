def solve(
        hourly_wage: float = 18.00, # Tina makes $18.00 an hour
        standard_shift_hours: int = 8, # If she works more than 8 hours per shift
        overtime_multiplier_fraction: float = 1/2, # 1/2 your hourly wage
        daily_work_hours: int = 10, # If she works 10 hours every day
        num_work_days: int = 5 # for 5 days
    ):
    """Index: 9.
    Returns: the total money Tina makes for working 5 days, including overtime.
    """
    #: L1
    pay_per_standard_shift = standard_shift_hours * hourly_wage

    #: L2
    overtime_hours_per_day = daily_work_hours - standard_shift_hours

    #: L3
    overtime_extra_rate = hourly_wage * overtime_multiplier_fraction

    #: L4
    overtime_hourly_wage = hourly_wage + overtime_extra_rate

    #: L5
    total_base_pay = pay_per_standard_shift * num_work_days

    #: L6
    daily_overtime_pay = overtime_hourly_wage * overtime_hours_per_day

    #: L7
    total_overtime_pay = daily_overtime_pay * num_work_days

    #: L8
    total_earnings = total_base_pay + total_overtime_pay

    answer = total_earnings # FINAL ANSWER
    return answer