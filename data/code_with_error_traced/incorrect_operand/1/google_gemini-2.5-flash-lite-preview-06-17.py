def solve(
    hourly_wage: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned.
    """

    #: L1
    wage_per_minute = minutes_worked / 60 # eval: 0.8333333333333334 = 50 / 60

    #: L2
    total_earned = wage_per_minute * minutes_worked # eval: 41.66666666666667 = 0.8333333333333334 * 50

    #: FA
    answer = total_earned
    return answer # eval: return 41.66666666666667
