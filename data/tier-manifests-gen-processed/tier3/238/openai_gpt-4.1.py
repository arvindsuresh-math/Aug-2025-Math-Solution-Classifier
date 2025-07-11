def solve():
    """Index: 238.
    Returns: the number of cookies Jack needs to sell to reach his goal.
    """
    # L1
    brownie_price = 3 # $3 each (brownies)
    brownies_sold = 4 # 4 brownies
    brownie_earnings = brownie_price * brownies_sold

    # L2
    lemon_square_price = 2 # $2 each (lemon squares)
    lemon_squares_sold = 5 # 5 lemon squares
    lemon_square_earnings = lemon_square_price * lemon_squares_sold

    # L3
    goal_amount = 50 # Jack's goal is to make $50
    remaining_needed = goal_amount - brownie_earnings - lemon_square_earnings

    # L4
    cookie_price = 4 # cookies for $4 each
    cookies_needed = remaining_needed / cookie_price

    # FA
    answer = cookies_needed
    return answer