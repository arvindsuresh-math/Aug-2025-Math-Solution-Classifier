def solve(
    hourly_wage: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned.
    """

    #: L1
    wage_per_minute = hourly_wage / 60 # eval: 0.2 = 12 / 60

    #: L2
    total_earned = wage_per_minute * minutes_worked # eval: 10.0 = 0.2 * 50

    #: FA
    answer = total_earned
    return answer # eval: return 10.0
