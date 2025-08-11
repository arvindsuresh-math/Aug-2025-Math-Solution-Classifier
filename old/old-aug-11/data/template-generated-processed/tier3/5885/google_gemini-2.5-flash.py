def solve():
    """Index: 5885.
    Returns: the total number of t-shirts made over two hours.
    """
    # L1
    minutes_per_hour = 60 # WK
    rate_first_hour_minutes = 12 # one every 12 minutes
    tshirts_first_hour = minutes_per_hour / rate_first_hour_minutes

    # L2
    rate_second_hour_minutes = 6 # every 6 minutes
    tshirts_second_hour = minutes_per_hour / rate_second_hour_minutes

    # L3
    total_tshirts = tshirts_first_hour + tshirts_second_hour

    # FA
    answer = total_tshirts
    return answer