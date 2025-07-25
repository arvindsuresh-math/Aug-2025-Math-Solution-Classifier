def solve(
    hourly_rate: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # She did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for her babysitting work.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2
    earnings = minutes_worked * minutes_worked # eval: 2500 = 50 * 50

    #: FA
    answer = earnings
    return answer # eval: return 2500
