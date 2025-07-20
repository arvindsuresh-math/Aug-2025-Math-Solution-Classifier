def solve():
    """Index: 5791.
    Returns: the number of additional miles Elroy will walk.
    """
    # L1
    last_year_winner_collected_money = 44 # last year's winner collected $44
    last_year_earnings_per_mile = 4 # walkers earned $4 a mile
    last_year_winner_miles = last_year_winner_collected_money / last_year_earnings_per_mile

    # L2
    elroy_target_collection = 44 # to collect the same amount of money (as last year's winner collected $44)
    elroy_earnings_per_mile = 2.75 # walkers earn $2.75 a mile
    elroy_miles = elroy_target_collection / elroy_earnings_per_mile

    # L3
    extra_miles_elroy_walks = elroy_miles - last_year_winner_miles

    # FA
    answer = extra_miles_elroy_walks
    return answer