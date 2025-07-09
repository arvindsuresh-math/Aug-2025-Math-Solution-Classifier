def solve(
    piano_practice_minutes_per_day: int = 20, # Carolyn practices the piano for 20 minutes a day
    violin_practice_multiplier: int = 3, # and the violin for three times as long
    practice_days_per_week: int = 6, # If she practice six days a week
    weeks_per_month: int = 4 # in a month with four weeks
):
    """Index: 46.
    Returns: the total number of minutes Carolyn spends practicing in a month."""

    #: L1
    violin_practice_minutes_per_day = piano_practice_minutes_per_day * violin_practice_multiplier # eval: 60 = 20 * 3

    #: L2

    #: L3
    total_practice_minutes_per_week = violin_practice_multiplier * practice_days_per_week # eval: 18 = 3 * 6

    #: L4
    total_practice_minutes_per_month = total_practice_minutes_per_week * weeks_per_month # eval: 72 = 18 * 4

    #: FA
    answer = total_practice_minutes_per_month
    return answer # eval: return 72
