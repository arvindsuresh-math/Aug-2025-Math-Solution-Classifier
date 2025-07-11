def solve():
    """Index: 1746.
    Returns: the total money the company pays per month after the new hires.
    """
    # L1
    pay_per_hour = 12 # each paid $12 per hour
    hours_per_day = 10 # working 10 hours a day
    pay_per_employee_per_day = pay_per_hour * hours_per_day

    # L2
    days_per_week = 5 # five days a week
    weeks_per_month = 4 # 4 weeks a month
    work_days_per_month = days_per_week * weeks_per_month

    # L3
    pay_per_employee_per_month = work_days_per_month * pay_per_employee_per_day

    # L4
    initial_employees = 500 # 500 employees
    new_hires = 200 # hired 200 more people
    total_employees = initial_employees + new_hires

    # L5
    total_monthly_pay = total_employees * pay_per_employee_per_month

    # FA
    answer = total_monthly_pay
    return answer