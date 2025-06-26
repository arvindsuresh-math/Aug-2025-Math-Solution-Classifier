def solve(
        daily_wage_no_bonus: int = 80, # He makes $80 a day
        work_hours_no_bonus: int = 8, # works for 8 hours
        performance_bonus: int = 20, # extra $20 a day
        extra_work_hours: int = 2 # 2-hour longer workday
    ):
    """Index: 91.
    Returns: John's hourly rate if he decides to earn the bonus.
    """

    #: L1
    total_work_hours_with_bonus = work_hours_no_bonus + extra_work_hours

    #: L2
    total_daily_pay_with_bonus = daily_wage_no_bonus + performance_bonus

    #: L3
    hourly_rate_with_bonus = total_daily_pay_with_bonus / total_work_hours_with_bonus

    answer = hourly_rate_with_bonus # FINAL ANSWER
    return answer