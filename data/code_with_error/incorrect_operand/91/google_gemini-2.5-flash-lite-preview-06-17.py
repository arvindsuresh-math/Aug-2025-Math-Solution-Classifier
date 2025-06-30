def solve(
    base_daily_pay: int = 80, # He makes $80 a day
    base_hours_per_day: int = 8, # and works for 8 hours
    bonus_pay_per_day: int = 20, # an extra $20 a day
    extra_hours_for_bonus: int = 2 # the extra effort results in a 2-hour longer workday
):
    """Index: 91.
    Returns: John's hourly rate if he decides to earn the bonus.
    """

    #: L1
    total_hours_with_bonus = base_hours_per_day + base_daily_pay

    #: L2
    total_daily_pay_with_bonus = base_daily_pay + bonus_pay_per_day

    #: L3
    hourly_rate_with_bonus = total_daily_pay_with_bonus / total_hours_with_bonus

    #: FA
    answer = hourly_rate_with_bonus
    return answer