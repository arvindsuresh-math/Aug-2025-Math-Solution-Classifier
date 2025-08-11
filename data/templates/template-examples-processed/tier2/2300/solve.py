def solve():
    """Index: 2300.
    Returns: the total amount the company pays for both workers in one month.
    """
    # L1
    josh_hours_per_day = 8 # 8 hours a day
    days_per_week = 5 # 5 days a week
    weeks_per_month = 4 # 4 weeks a month
    josh_hours_per_month = josh_hours_per_day * days_per_week * weeks_per_month

    # L2
    josh_hourly_rate = 9 # $9 an hour
    josh_monthly_pay = josh_hours_per_month * josh_hourly_rate

    # L3
    carl_less_hours_per_day = 2 # 2 hours less than Josh
    carl_hours_per_day = josh_hours_per_day - carl_less_hours_per_day
    carl_hours_per_month = carl_hours_per_day * days_per_week * weeks_per_month

    # L4
    carl_hourly_rate = 4.5 # half that (of $9)
    carl_monthly_pay = carl_hours_per_month * carl_hourly_rate

    # L5
    total_pay = josh_monthly_pay + carl_monthly_pay

    # FA
    answer = total_pay
    return answer