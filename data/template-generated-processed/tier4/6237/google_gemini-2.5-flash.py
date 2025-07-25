def solve():
    """Index: 6237.
    Returns: the amount of money Brendan pays in taxes each week.
    """
    # L1
    num_8hr_shifts = 2 # 2 8-hour shifts
    hours_per_8hr_shift = 8 # 8-hour shifts
    total_hours_8hr_shifts = num_8hr_shifts * hours_per_8hr_shift

    # L2
    hours_12hr_shift = 12 # 1 12-hour shift
    total_hours_worked = total_hours_8hr_shifts + hours_12hr_shift

    # L3
    hourly_wage = 6 # $6/hour as a waiter
    total_wage_earnings = hourly_wage * total_hours_worked

    # L4
    tips_per_hour = 12 # $12 in tips each hour
    total_tips_earned = tips_per_hour * total_hours_worked

    # L5
    tips_report_divisor = 3 # only reports 1/3rd of his tips
    reported_tips = total_tips_earned / tips_report_divisor

    # L6
    total_reported_income = total_wage_earnings + reported_tips

    # L7
    tax_rate = 0.2 # 20% of his income in taxes
    taxes_paid = total_reported_income * tax_rate

    # FA
    answer = taxes_paid
    return answer