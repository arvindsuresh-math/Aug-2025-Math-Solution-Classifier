def solve():
    """Index: 6780.
    Returns: how long Erica can stay on the merry-go-round.
    """
    # L1
    dave_ride_time = 10 # 10 minutes
    chuck_ride_multiplier = 5 # 5 times longer
    chuck_ride_time = dave_ride_time * chuck_ride_multiplier

    # L2
    erica_longer_percent_decimal = 0.30 # from solution text: .30*50
    erica_longer_percent_num = 30 # 30% longer
    percent_factor = 0.01 # WK
    erica_extra_time = erica_longer_percent_num * percent_factor * chuck_ride_time

    # L3
    erica_total_time = chuck_ride_time + erica_extra_time

    # FA
    answer = erica_total_time
    return answer