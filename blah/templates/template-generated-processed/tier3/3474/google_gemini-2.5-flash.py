def solve():
    """Index: 3474.
    Returns: the average number of seconds Heather can take to pick a weed.
    """
    # L1
    hourly_wage_dollars = 10 # earn $10 an hour
    cents_per_dollar = 100 # 100 cents / $1
    cents_needed_per_hour = hourly_wage_dollars * cents_per_dollar

    # L2
    cents_per_weed = 5 # 5 cents for every weed
    weeds_per_hour = cents_needed_per_hour / cents_per_weed

    # L3
    minutes_per_hour = 60 # 60 minutes / 1 hr
    minutes_in_hour = 1 * minutes_per_hour

    # L4
    seconds_per_minute = 60 # 60 seconds / 1 minute
    seconds_in_hour = minutes_in_hour * seconds_per_minute

    # L5
    seconds_per_weed = seconds_in_hour / weeds_per_hour

    # FA
    answer = seconds_per_weed
    return answer