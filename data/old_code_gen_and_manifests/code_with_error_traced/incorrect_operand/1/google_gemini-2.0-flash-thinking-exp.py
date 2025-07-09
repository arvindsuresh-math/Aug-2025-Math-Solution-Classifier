def solve(
    hourly_rate: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the total amount Weng earned for babysitting.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2
    total_earnings = hourly_rate * minutes_worked # eval: 600 = 12 * 50

    #: FA
    answer = total_earnings
    return answer # eval: return 600
