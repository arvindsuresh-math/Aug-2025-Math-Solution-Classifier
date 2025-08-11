def solve():
    """Index: 6734.
    Returns: the number of cookies Katrina has left to take home.
    """
    # L1
    dozen_cookies = 12 # WK
    morning_dozen_sold = 3 # sells 3 dozen cookies
    morning_cookies_sold = dozen_cookies * morning_dozen_sold

    # L2
    lunch_cookies_sold = 57 # sells 57 cookies
    afternoon_cookies_sold = 16 # sells 16 more cookies
    total_cookies_sold = morning_cookies_sold + lunch_cookies_sold + afternoon_cookies_sold

    # L3
    initial_cookies = 120 # Katrina has 120 cookies
    cookies_left = initial_cookies - total_cookies_sold

    # FA
    answer = cookies_left
    return answer