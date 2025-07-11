def solve(
        piano_practice_time: int = 20,  # Carolyn practices the piano for 20 minutes a day
        violin_practice_multiplier: int = 3,  # violin for three times as long
        practice_days_per_week: int = 6,  # she practices six days a week
        weeks_in_month: int = 4  # a month with four weeks
    ):
    """Index: 46.
    Returns: the total number of minutes Carolyn spends practicing in a month.
    """
    #: L1
    violin_practice_time = piano_practice_time * violin_practice_multiplier

    #: L2
    total_daily_practice = violin_practice_time + piano_practice_time

    #: L3
    total_weekly_practice = total_daily_practice * practice_days_per_week

    #: L4
    total_monthly_practice = total_weekly_practice * weeks_in_month

    answer = total_monthly_practice  # FINAL ANSWER
    return answer