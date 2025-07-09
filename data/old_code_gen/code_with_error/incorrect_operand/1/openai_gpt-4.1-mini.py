def solve(
    hourly_wage: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # she did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for babysitting 50 minutes.
    """

    #: L1
    wage_per_minute = hourly_wage / 60

    #: L2
    earnings = wage_per_minute * hourly_wage

    #: FA
    answer = earnings
    return answer