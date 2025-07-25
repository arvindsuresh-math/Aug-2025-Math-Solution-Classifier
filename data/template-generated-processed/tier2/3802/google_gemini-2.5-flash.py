def solve():
    """Index: 3802.
    Returns: the money left on her card after a week of coffee and pastry.
    """
    # L1
    latte_cost = 3.75 # latte that cost $3.75
    croissant_cost = 3.50 # croissant for $3.50
    daily_cost = latte_cost + croissant_cost

    # L2
    num_days_in_week = 7 # for a week
    weekly_food_cost = daily_cost * num_days_in_week

    # L3
    num_cookies = 5 # buy 5 cookies
    cookie_cost = 1.25 # $1.25 each
    total_cookie_cost = num_cookies * cookie_cost

    # L4
    gift_card_value = 100 # $100 gift card
    remaining_balance = gift_card_value - weekly_food_cost - total_cookie_cost

    # FA
    answer = remaining_balance
    return answer