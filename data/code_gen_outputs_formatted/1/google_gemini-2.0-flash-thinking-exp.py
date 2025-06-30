def solve(
    hourly_rate: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the total amount Weng earned for babysitting.
    """

    #: L1
    rate_per_minute = hourly_rate / 60

    #: L2
    total_earnings = rate_per_minute * minutes_worked

    #: FA
    answer = total_earnings
    return answer