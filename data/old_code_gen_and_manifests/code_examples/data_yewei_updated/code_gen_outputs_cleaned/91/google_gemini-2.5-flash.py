def solve(
        daily_wage_base: int = 80, # He makes $80 a day
        daily_hours_base: int = 8, # works for 8 hours
        bonus_amount: int = 20, # extra $20 a day
        extra_hours_for_bonus: int = 2 # 2-hour longer workday
    ):
    """Index: 91.
    Returns: how much John makes per hour if he decides to earn the bonus.
    """
    #: L1
    total_hours_with_bonus = daily_hours_base + extra_hours_for_bonus

    #: L2
    total_pay_with_bonus = daily_wage_base + bonus_amount

    #: L3
    hourly_rate_with_bonus = total_pay_with_bonus / total_hours_with_bonus

    answer = hourly_rate_with_bonus # FINAL ANSWER
    return answer