def solve():
    """Index: 5360.
    Returns: the number of hamburgers Tonya needs to eat to beat last year's winner.
    """
    # L1
    ounces_last_year_winner_ate = 84 # Last year the winner ate 84 ounces
    ounces_per_hamburger = 4 # Each hamburger is 4 ounces
    hamburgers_last_year_winner_ate = ounces_last_year_winner_ate / ounces_per_hamburger

    # L2
    one_more_hamburger = 1 # WK
    hamburgers_tonya_needs_to_eat = hamburgers_last_year_winner_ate + one_more_hamburger

    # FA
    answer = hamburgers_tonya_needs_to_eat
    return answer