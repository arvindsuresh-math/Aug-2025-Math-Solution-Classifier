def solve():
    """Index: 1746.
    Returns: the total monthly payroll after the new hires.
    """
    # L1
    hourly_wage = 12 # $12 per hour
    hours_per_day = 10 # 10 hours a day
    daily_pay_per_employee = hourly_wage * hours_per_day

    # L2
    days_per_week = 5 # five days a week
    weeks_per_month = 4 # 4 weeks a month
    days_per_month = days_per_week * weeks_per_month

    # L3
    monthly_pay_per_employee = days_per_month * daily_pay_per_employee

    # L4
    initial_employees = 500 # 500 employees
    new_hires = 200 # hired 200 more people
    total_employees = initial_employees + new_hires

    # L5
    total_monthly_pay = total_employees * monthly_pay_per_employee

    # FA
    answer = total_monthly_pay
    return answer