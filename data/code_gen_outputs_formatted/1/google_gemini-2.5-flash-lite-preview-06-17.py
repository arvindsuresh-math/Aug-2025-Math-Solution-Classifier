def solve(
    hourly_wage: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned.
    """

    #: L1
    wage_per_minute = hourly_wage / 60

    #: L2
    total_earned = wage_per_minute * minutes_worked

    #: FA
    answer = total_earned
    return answer