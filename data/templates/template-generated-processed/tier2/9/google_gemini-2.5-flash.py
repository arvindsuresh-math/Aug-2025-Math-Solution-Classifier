def solve():
    """Index: 9.
    Returns: the total money Tina makes.
    """
    # L1
    regular_hours_per_day = 8 # more than 8 hours per shift
    hourly_wage = 18.00 # $18.00 an hour
    regular_daily_pay = regular_hours_per_day * hourly_wage

    # L2
    total_hours_per_day = 10 # works 10 hours every day
    overtime_hours_per_day = total_hours_per_day - regular_hours_per_day

    # L3
    overtime_factor = 0.5 # 1/2 your hourly wage
    overtime_additional_pay_per_hour = hourly_wage * overtime_factor

    # L4
    overtime_hourly_wage = hourly_wage + overtime_additional_pay_per_hour

    # L5
    num_days_worked = 5 # for 5 days
    total_regular_pay = regular_daily_pay * num_days_worked

    # L6
    daily_overtime_pay = overtime_hourly_wage * overtime_hours_per_day

    # L7
    total_overtime_pay = daily_overtime_pay * num_days_worked

    # L8
    total_money_made = total_regular_pay + total_overtime_pay

    # FA
    answer = total_money_made
    return answer