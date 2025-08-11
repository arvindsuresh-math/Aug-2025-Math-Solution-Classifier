def solve():
    """Index: 2271.
    Returns: the number of people who will run this year.
    """
    # L1
    signed_up_last_year = 200 # 200 people signed up
    no_show_last_year = 40 # Forty people did not show up to run
    runners_last_year = signed_up_last_year - no_show_last_year

    # L2
    multiplier_this_year = 2 # twice as many runners
    runners_this_year = multiplier_this_year * runners_last_year

    # FA
    answer = runners_this_year
    return answer