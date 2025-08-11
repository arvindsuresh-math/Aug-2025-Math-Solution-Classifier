def solve():
    """Index: 4493.
    Returns: the amount Janet earns per hour in dollars.
    """
    # L1
    hours_in_calculation = 1 # WK
    minutes_per_hour = 60 # WK
    seconds_per_minute = 60 # WK
    seconds_per_hour = hours_in_calculation * minutes_per_hour * seconds_per_minute

    # L2
    seconds_per_post = 10 # 10 seconds to check a post
    posts_per_hour = seconds_per_hour / seconds_per_post

    # L3
    pay_per_post_dollars = 0.25 # 25 cents per post
    hourly_pay = pay_per_post_dollars * posts_per_hour

    # FA
    answer = hourly_pay
    return answer