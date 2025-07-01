def solve(
    hourly_rate: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the total amount Weng earned for babysitting.
    """

    #: L1
    rate_per_minute = -9.8 # eval: -9.8 = -9.8

    #: L2
    total_earnings = rate_per_minute * minutes_worked # eval: -490.00000000000006 = -9.8 * 50

    #: FA
    answer = total_earnings
    return answer # eval: return -490.00000000000006
