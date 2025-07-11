def solve():
    """Index: 2300.
    Returns: the total amount the company pays for Josh and Carl in one month.
    """
    # L1
    josh_hours_per_day = 8 # Josh works 8 hours a day
    days_per_week = 5 # 5 days a week
    weeks_per_month = 4 # 4 weeks a month
    josh_monthly_hours = josh_hours_per_day * days_per_week * weeks_per_month

    # L2
    josh_hourly_rate = 9 # Josh gets $9 an hour
    josh_monthly_earnings = josh_monthly_hours * josh_hourly_rate

    # L3
    carl_hours_less_than_josh = 2 # works 2 hours less than Josh every day
    carl_hours_per_day = josh_hours_per_day - carl_hours_less_than_josh
    carl_monthly_hours = carl_hours_per_day * days_per_week * weeks_per_month

    # L4
    carl_hourly_rate = josh_hourly_rate / 2 # Carl, half that
    carl_monthly_earnings = carl_monthly_hours * carl_hourly_rate

    # L5
    total_monthly_payment = josh_monthly_earnings + carl_monthly_earnings

    # FA
    answer = total_monthly_payment
    return answer