def solve():
    """Index: 3867.
    Returns: the amount of pay Susan will miss on her vacation.
    """
    # L1
    vacation_weeks = 2 # two week vacation
    work_days_per_week = 5 # works five days a week
    total_workdays_vacation = vacation_weeks * work_days_per_week

    # L2
    paid_vacation_days = 6 # six days of paid vacation
    unpaid_vacation_days = total_workdays_vacation - paid_vacation_days

    # L3
    pay_per_hour = 15 # $15 per hour
    hours_per_day = 8 # works 8 hours a day
    pay_per_day = pay_per_hour * hours_per_day

    # L4
    missed_pay = pay_per_day * unpaid_vacation_days

    # FA
    answer = missed_pay
    return answer