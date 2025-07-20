def solve():
    """Index: 6081.
    Returns: the cost to make the cookies.
    """
    # L1
    total_earned = 60 # earned $60
    num_cookies_sold = 50 # sold 50 cookies
    price_per_cookie_sold = total_earned / num_cookies_sold

    # L2
    markup_factor = 1.2 # 20% more than it costs to make them (1 + 0.20)
    cost_per_cookie_to_make = price_per_cookie_sold / markup_factor

    # FA
    answer = cost_per_cookie_to_make
    return answer