def solve():
    """Index: 9.
    Returns: the total amount of money Tina makes in 5 days with overtime.
    """
    # L1
    regular_hours_per_day = 8 # 8 hours a day
    hourly_wage = 18.00 # $18 per hour
    base_pay_per_shift = regular_hours_per_day * hourly_wage

    # L2
    total_hours_per_day = 10 # 10 hours a day
    overtime_hours_per_day = total_hours_per_day - regular_hours_per_day

    # L3
    overtime_multiplier = 0.5 # 1/2 your hourly wage
    overtime_extra_per_hour = hourly_wage * overtime_multiplier

    # L4
    overtime_hourly_rate = hourly_wage + overtime_extra_per_hour

    # L5
    num_days = 5 # 5 days
    total_base_pay = num_days * base_pay_per_shift

    # L6
    overtime_pay_per_day = overtime_hourly_rate * overtime_hours_per_day

    # L7
    total_overtime_pay = overtime_pay_per_day * num_days

    # L8
    total_pay = total_base_pay + total_overtime_pay

    # FA
    answer = total_pay
    return answer