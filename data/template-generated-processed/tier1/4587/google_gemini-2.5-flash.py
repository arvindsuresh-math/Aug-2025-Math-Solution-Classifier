def solve():
    """Index: 4587.
    Returns: the number of bracelets Chantel has in the end.
    """
    # L1
    first_period_days = 5 # For 5 days
    bracelets_per_day_first_period = 2 # makes 2 friendship bracelets every day
    bracelets_after_first_period = first_period_days * bracelets_per_day_first_period

    # L2
    given_away_first_time = 3 # gives away 3 bracelets
    bracelets_after_first_giveaway = bracelets_after_first_period - given_away_first_time

    # L3
    second_period_days = 4 # for four days
    bracelets_per_day_second_period = 3 # makes 3 friendship bracelets every day
    bracelets_made_second_period = second_period_days * bracelets_per_day_second_period

    # L4
    given_away_second_time = 6 # gives away 6 bracelets
    final_bracelets = bracelets_after_first_giveaway + bracelets_made_second_period - given_away_second_time

    # FA
    answer = final_bracelets
    return answer