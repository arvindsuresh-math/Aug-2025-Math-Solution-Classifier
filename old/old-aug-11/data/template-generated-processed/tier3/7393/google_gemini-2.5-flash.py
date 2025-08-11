def solve():
    """Index: 7393.
    Returns: the number of cookies Paul took out in four days.
    """
    # L1
    initial_cookies = 70 # 70 cookies in a jar
    remaining_cookies = 28 # 28 cookies left after a week
    cookies_taken_in_a_week = initial_cookies - remaining_cookies

    # L2
    days_in_a_week = 7 # in a week
    cookies_per_day = cookies_taken_in_a_week / days_in_a_week

    # L3
    target_days = 4 # in four days
    cookies_taken_in_four_days = cookies_per_day * target_days

    # FA
    answer = cookies_taken_in_four_days
    return answer