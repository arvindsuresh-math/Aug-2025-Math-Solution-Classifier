def solve():
    """Index: 7327.
    Returns: the difference in the number of cookies and brownies remaining after a week.
    """
    # L1
    days_in_week = 7 # WK
    cookies_per_day = 3 # eats 3 cookies a day
    cookies_eaten_week = days_in_week * cookies_per_day

    # L2
    brownies_per_day = 1 # and 1 brownie a day
    brownies_eaten_week = days_in_week * brownies_per_day

    # L3
    initial_cookies = 60 # starts with 60 cookies
    cookies_remaining = initial_cookies - cookies_eaten_week

    # L4
    initial_brownies = 10 # and 10 brownies
    brownies_remaining = initial_brownies - brownies_eaten_week

    # L5
    difference_cookies_brownies = cookies_remaining - brownies_remaining

    # FA
    answer = difference_cookies_brownies
    return answer