def solve(
        base_daily_wage: int = 80,  # John makes $80 a day
        base_hours: int = 8,  # and works for 8 hours
        bonus_amount: int = 20,  # performance bonus of an extra $20 a day
        bonus_hours: int = 2  # extra effort results in a 2-hour longer workday
    ):
    """Index: 91.
    Returns: John's hourly wage when working for the performance bonus.
    """

    #: L1
    total_hours_with_bonus = base_hours * bonus_hours # eval: 16 = 8 * 2

    #: L2
    total_daily_wage_with_bonus = base_daily_wage + bonus_amount # eval: 100 = 80 + 20

    #: L3
    hourly_rate_with_bonus = total_daily_wage_with_bonus / total_hours_with_bonus # eval: 6.25 = 100 / 16

    #: FA
    answer = hourly_rate_with_bonus
    return answer # eval: return 6.25
