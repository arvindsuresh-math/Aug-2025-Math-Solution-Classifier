from fractions import Fraction

def solve():
    """Index: 3550.
    Returns: the total money Porter will earn after a month.
    """
    # L1
    daily_rate = 8 # Porter earns $8 per day
    work_days_per_week = 5 # works 5 times a week
    weekly_earning = daily_rate * work_days_per_week

    # L2
    weeks_per_month = 4 # WK
    monthly_earning_regular = weekly_earning * weeks_per_month

    # L3
    overtime_rate_percentage = Fraction(50, 100) # an extra fifty percent
    extra_overtime_amount_per_day = daily_rate * overtime_rate_percentage

    # L4
    overtime_daily_rate = daily_rate + extra_overtime_amount_per_day

    # L5
    total_overtime_monthly_pay = overtime_daily_rate * weeks_per_month

    # L6
    total_monthly_earning = monthly_earning_regular + total_overtime_monthly_pay

    # FA
    answer = total_monthly_earning
    return answer