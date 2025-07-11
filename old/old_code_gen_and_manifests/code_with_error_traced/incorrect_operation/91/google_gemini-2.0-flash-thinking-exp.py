def solve(
    daily_wage: int = 80, # He makes $80 a day
    regular_hours_per_day: int = 8, # works for 8 hours
    bonus_amount: int = 20, # performance bonus of an extra $20 a day
    extra_hours_for_bonus: int = 2 # the extra effort results in a 2-hour longer workday
):
    """Index: 91.
    Returns: John's hourly wage when earning the bonus.
    """

    #: L1
    bonus_workday_hours = regular_hours_per_day - extra_hours_for_bonus # eval: 6 = 8 - 2

    #: L2
    total_daily_pay_with_bonus = daily_wage + bonus_amount # eval: 100 = 80 + 20

    #: L3
    hourly_rate_with_bonus = total_daily_pay_with_bonus / bonus_workday_hours # eval: 16.666666666666668 = 100 / 6

    #: FA
    answer = hourly_rate_with_bonus
    return answer # eval: return 16.666666666666668
