def solve():
    """Index: 5245.
    Returns: the amount of profit each charity gets.
    """
    # L1
    num_dozens = 6 # 6 dozen cookies
    cookies_per_dozen = 12 # WK
    total_cookies = num_dozens * cookies_per_dozen

    # L2
    selling_price_per_cookie = 1.5 # sells each cookie for $1.5
    cost_per_cookie = 0.25 # each cookie costs $0.25 to make
    profit_per_cookie = selling_price_per_cookie - cost_per_cookie

    # L3
    total_profit = total_cookies * profit_per_cookie

    # L4
    num_charities = 2 # splits the profit between two charities evenly
    profit_per_charity = total_profit / num_charities

    # FA
    answer = profit_per_charity
    return answer