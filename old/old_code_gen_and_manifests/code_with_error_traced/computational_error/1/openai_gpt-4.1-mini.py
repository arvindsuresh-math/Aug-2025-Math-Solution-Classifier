def solve(
    hourly_wage: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # she did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for babysitting 50 minutes.
    """

    #: L1
    wage_per_minute = -9.8 # eval: -9.8 = -9.8

    #: L2
    earnings = wage_per_minute * minutes_worked # eval: -490.00000000000006 = -9.8 * 50

    #: FA
    answer = earnings
    return answer # eval: return -490.00000000000006
