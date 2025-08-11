def solve():
    """Index: 6101.
    Returns: the number of additional weekends Cary needs to mow lawns.
    """
    # L1
    shoe_cost = 120 # shoes that cost $120
    already_saved = 30 # He has already saved $30
    money_needed = shoe_cost - already_saved

    # L2
    earnings_per_lawn = 5 # He earns $5 for every lawn he mows
    lawns_per_weekend = 3 # mows 3 lawns each weekend
    earnings_per_weekend = earnings_per_lawn * lawns_per_weekend

    # L3
    weekends_needed = money_needed / earnings_per_weekend

    # FA
    answer = weekends_needed
    return answer