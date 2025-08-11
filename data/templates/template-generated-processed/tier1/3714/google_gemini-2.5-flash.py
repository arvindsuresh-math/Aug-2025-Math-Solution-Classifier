def solve():
    """Index: 3714.
    Returns: how much more money Jacob needs to go to Brickville.
    """
    # L1
    hourly_wage = 20 # earning $20 per hour
    hours_worked = 10 # works 10 hours
    earnings_from_job = hourly_wage * hours_worked

    # L2
    cookie_price = 4 # sell cookies for $4 each
    cookies_sold = 24 # sells 24 pieces of cookies
    earnings_from_cookies = cookie_price * cookies_sold

    # L3
    total_earned_so_far = earnings_from_job + earnings_from_cookies

    # L4
    lottery_ticket_cost = 10 # buys a lottery ticket for $10
    money_after_ticket = total_earned_so_far - lottery_ticket_cost

    # L5
    lottery_win = 500 # wins $500
    money_after_win = lottery_win + money_after_ticket

    # L6
    gift_per_sister = 500 # gets $500 from both of his sisters
    num_sisters = 2 # WK
    total_gift_from_sisters = gift_per_sister * num_sisters

    # L7
    final_money_saved = total_gift_from_sisters + money_after_win

    # L8
    total_needed = 5000 # needs to have $5000 total
    money_needed_more = total_needed - final_money_saved

    # FA
    answer = money_needed_more
    return answer